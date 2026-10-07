import { DECKS } from './decks.js';

// --- DETECT PLATFORM ---
const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) ||
  (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);

// --- GAME STATE ---
const state = {
  activeTab: 'kids', // 'kids' | 'adults' | 'custom'
  roundDuration: 60, // seconds
  currentDeck: null,
  wordsQueue: [],
  currentWordIndex: 0,
  score: 0,
  correctWords: [],
  passedWords: [],
  timerInterval: null,
  timeLeft: 60,
  isPlaying: false,
  isLocked: false, // debounce lock between words
  motionState: 'NEUTRAL', // 'NEUTRAL' | 'UP' | 'DOWN'
  permissionGranted: !isIOS, // Android/Desktop don't need explicit requestPermission()
  wakeLock: null,
  customDecks: [],
  settings: {
    sound: true,
    vibration: true,
    touchEnabled: true,
    invertTilt: false,
    sensitivity: 'medium', // 'high' | 'medium' | 'low'
  },
  // Sensor debug values
  sensorData: {
    accZ: 0,
    accX: 0,
    accY: 0,
    beta: 0,
    gamma: 0,
    source: 'none', // 'motion' | 'orientation'
    currentGesture: 'NEUTRAL'
  }
};

// --- AUDIO SYNTHESIZER (Web Audio API) ---
let audioCtx = null;

function initAudio() {
  if (!audioCtx) {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (AudioContext) {
      audioCtx = new AudioContext();
    }
  }
  if (audioCtx && audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
}

function playTone(freq, duration, type = 'sine', gainVal = 0.25) {
  if (!state.settings.sound || !audioCtx) return;
  try {
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = type;
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
    gain.gain.setValueAtTime(gainVal, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + duration);
  } catch (e) {
    console.warn("Audio play error", e);
  }
}

function playCountdownBeep() {
  playTone(523.25, 0.12, 'sine', 0.2); // C5
}

function playStartChime() {
  if (!state.settings.sound || !audioCtx) return;
  playTone(523.25, 0.1, 'sine', 0.25);
  setTimeout(() => playTone(659.25, 0.1, 'sine', 0.25), 90);
  setTimeout(() => playTone(783.99, 0.35, 'triangle', 0.3), 180);
}

function playCorrectSound() {
  if (!state.settings.sound || !audioCtx) return;
  playTone(659.25, 0.1, 'sine', 0.3); // E5
  setTimeout(() => playTone(880.00, 0.25, 'sine', 0.35), 90); // A5
}

function playPassSound() {
  if (!state.settings.sound || !audioCtx) return;
  playTone(329.63, 0.12, 'sawtooth', 0.18); // E4
  setTimeout(() => playTone(246.94, 0.22, 'sawtooth', 0.18), 100); // B3
}

function playGameOverSound() {
  if (!state.settings.sound || !audioCtx) return;
  playTone(440, 0.15, 'square', 0.2);
  setTimeout(() => playTone(349.23, 0.15, 'square', 0.2), 150);
  setTimeout(() => playTone(293.66, 0.5, 'square', 0.25), 300);
}

function triggerHaptic(type) {
  if (!state.settings.vibration || !navigator.vibrate) return;
  if (type === 'correct') {
    navigator.vibrate([120]);
  } else if (type === 'pass') {
    navigator.vibrate([70, 50, 70]);
  }
}

// --- WAKE LOCK (Keep screen on) ---
async function requestWakeLock() {
  if ('wakeLock' in navigator) {
    try {
      state.wakeLock = await navigator.wakeLock.request('screen');
    } catch (err) {
      console.log('Wake Lock request error:', err);
    }
  }
}

function releaseWakeLock() {
  if (state.wakeLock) {
    state.wakeLock.release().then(() => {
      state.wakeLock = null;
    }).catch(() => {});
  }
}

// --- CUSTOM DECKS LOCALSTORAGE ---
function loadCustomDecks() {
  try {
    const stored = localStorage.getItem('headsup_custom_decks');
    if (stored) {
      state.customDecks = JSON.parse(stored);
    }
  } catch (e) {
    state.customDecks = [];
  }
}

function saveCustomDecks() {
  try {
    localStorage.setItem('headsup_custom_decks', JSON.stringify(state.customDecks));
  } catch (e) {
    console.error('Failed to save custom decks', e);
  }
}

// --- DOM ELEMENTS ---
const elements = {
  tabBtns: document.querySelectorAll('.tab-btn'),
  timerPills: document.getElementById('timer-pills'),
  decksContainer: document.getElementById('decks-container'),
  soundBtn: document.getElementById('sound-btn'),
  sensorTestBtn: document.getElementById('sensor-test-btn'),
  settingsBtn: document.getElementById('settings-btn'),
  iosPermissionBanner: document.getElementById('ios-permission-banner'),
  bannerPermissionBtn: document.getElementById('banner-permission-btn'),
  readyOverlay: document.getElementById('ready-overlay'),
  readyDeckTitle: document.getElementById('ready-deck-title'),
  readyStartBtn: document.getElementById('ready-start-btn'),
  readyCancelBtn: document.getElementById('ready-cancel-btn'),
  countdownScreen: document.getElementById('countdown-screen'),
  countdownDigit: document.getElementById('countdown-digit'),
  gameplayView: document.getElementById('gameplay-view'),
  gameDeckName: document.getElementById('game-deck-name'),
  gameTimerDisplay: document.getElementById('game-timer-display'),
  gameScoreDisplay: document.getElementById('game-score-display'),
  gameTiltBadge: document.getElementById('game-tilt-badge'),
  gameTiltText: document.getElementById('game-tilt-text'),
  currentWordText: document.getElementById('current-word-text'),
  currentWordHint: document.getElementById('current-word-hint'),
  actionFlash: document.getElementById('action-flash'),
  touchPassZone: document.getElementById('touch-pass-zone'),
  touchCorrectZone: document.getElementById('touch-correct-zone'),
  gameQuitBtn: document.getElementById('game-quit-btn'),
  resultsScreen: document.getElementById('results-screen'),
  finalScoreVal: document.getElementById('final-score-val'),
  resultsDeckName: document.getElementById('results-deck-name'),
  resultsWordList: document.getElementById('results-word-list'),
  resultsReplayBtn: document.getElementById('results-replay-btn'),
  resultsLobbyBtn: document.getElementById('results-lobby-btn'),
  sensorModal: document.getElementById('sensor-modal'),
  sensorPermissionStatus: document.getElementById('sensor-permission-status'),
  testTiltStatus: document.getElementById('test-tilt-status'),
  testSensorRaw: document.getElementById('test-sensor-raw'),
  requestPermissionBtn: document.getElementById('request-permission-btn'),
  customModal: document.getElementById('custom-modal'),
  customDeckForm: document.getElementById('custom-deck-form'),
  settingsModal: document.getElementById('settings-modal'),
  settingSoundToggle: document.getElementById('setting-sound-toggle'),
  settingVibrateToggle: document.getElementById('setting-vibrate-toggle'),
  settingInvertToggle: document.getElementById('setting-invert-toggle'),
  settingSensitivitySelect: document.getElementById('setting-sensitivity-select'),
  settingTouchToggle: document.getElementById('setting-touch-toggle'),
  toast: document.getElementById('toast')
};

// --- TOAST NOTIFICATIONS ---
function showToast(msg) {
  elements.toast.textContent = msg;
  elements.toast.classList.add('show');
  setTimeout(() => {
    elements.toast.classList.remove('show');
  }, 2200);
}

// --- PERMISSIONS MANAGEMENT (CRUCIAL FOR IPHONE) ---
function updatePermissionUI() {
  if (state.permissionGranted) {
    if (elements.iosPermissionBanner) {
      elements.iosPermissionBanner.style.display = 'none';
    }
    if (elements.sensorPermissionStatus) {
      elements.sensorPermissionStatus.innerHTML = `🟢 Motion Permission: <strong>Active & Granted</strong>`;
      elements.sensorPermissionStatus.style.background = 'rgba(16, 185, 129, 0.2)';
      elements.sensorPermissionStatus.style.color = '#34d399';
    }
    if (elements.requestPermissionBtn) {
      elements.requestPermissionBtn.textContent = 'Permission Granted ✓';
      elements.requestPermissionBtn.style.opacity = '0.6';
      elements.requestPermissionBtn.disabled = true;
    }
  } else {
    if (isIOS && elements.iosPermissionBanner) {
      elements.iosPermissionBanner.style.display = 'flex';
    }
    if (elements.sensorPermissionStatus) {
      elements.sensorPermissionStatus.innerHTML = `⚠️ Motion Permission: <strong>Not Yet Granted</strong> (Tap button below)`;
      elements.sensorPermissionStatus.style.background = 'rgba(245, 158, 11, 0.2)';
      elements.sensorPermissionStatus.style.color = '#fbbf24';
    }
    if (elements.requestPermissionBtn) {
      elements.requestPermissionBtn.textContent = 'Allow iPhone Motion Sensors';
      elements.requestPermissionBtn.style.opacity = '1';
      elements.requestPermissionBtn.disabled = false;
    }
  }
}

/**
 * MUST be executed synchronously on user click/tap to satisfy iOS Safari security policy.
 */
function requestIOSPermissionSync() {
  initAudio();

  let requested = false;

  if (typeof DeviceOrientationEvent !== 'undefined' && typeof DeviceOrientationEvent.requestPermission === 'function') {
    requested = true;
    DeviceOrientationEvent.requestPermission()
      .then((res) => {
        if (res === 'granted') {
          state.permissionGranted = true;
          updatePermissionUI();
          showToast('Motion sensors enabled! 📐');
        } else {
          showToast('Motion permission denied');
        }
      })
      .catch((err) => {
        console.warn('Orientation permission error:', err);
      });
  }

  if (typeof DeviceMotionEvent !== 'undefined' && typeof DeviceMotionEvent.requestPermission === 'function') {
    requested = true;
    DeviceMotionEvent.requestPermission()
      .then((res) => {
        if (res === 'granted') {
          state.permissionGranted = true;
          updatePermissionUI();
        }
      })
      .catch((err) => {
        console.warn('Motion permission error:', err);
      });
  }

  if (!requested) {
    // Non-iOS or older browser that does not require explicit request
    state.permissionGranted = true;
    updatePermissionUI();
  }
}

// Bind permission request to all user-action entrypoints
elements.bannerPermissionBtn.onclick = () => requestIOSPermissionSync();
elements.requestPermissionBtn.onclick = () => requestIOSPermissionSync();

// --- RENDER DECKS ---
function renderDecks() {
  elements.decksContainer.innerHTML = '';

  let deckList = [];
  if (state.activeTab === 'kids') {
    deckList = DECKS.kids;
  } else if (state.activeTab === 'adults') {
    deckList = DECKS.adults;
  } else if (state.activeTab === 'custom') {
    deckList = state.customDecks;
  }

  if (state.activeTab === 'custom') {
    // Add "Create New Deck" card
    const addCard = document.createElement('div');
    addCard.className = 'custom-deck-add-card';
    addCard.innerHTML = `
      <div class="custom-add-icon">➕</div>
      <div style="font-weight: 700; font-size: 1.1rem;">Create Custom Deck</div>
      <div style="font-size: 0.85rem; color: var(--text-muted);">Add your own words for friends or family</div>
    `;
    addCard.onclick = () => openModal('custom-modal');
    elements.decksContainer.appendChild(addCard);
  }

  if (deckList.length === 0 && state.activeTab === 'custom') {
    return;
  }

  deckList.forEach((deck) => {
    const card = document.createElement('div');
    card.className = 'deck-card';
    const glowColor = deck.color || '#6366f1';
    const wordCount = deck.words ? deck.words.length : 0;

    card.innerHTML = `
      <div class="deck-card-glow" style="background: ${glowColor};"></div>
      <div>
        <div class="deck-header">
          <div class="deck-icon">${deck.icon || '🎯'}</div>
          <span class="deck-badge">${wordCount} words</span>
        </div>
        <div class="deck-title">${deck.name}</div>
        <div class="deck-desc">${deck.description || 'Custom deck of words to guess!'}</div>
      </div>
      <button class="play-deck-btn" data-deck-id="${deck.id}">
        PLAY DECK <span>▶</span>
      </button>
    `;

    const playBtn = card.querySelector('.play-deck-btn');
    playBtn.onclick = (e) => {
      e.stopPropagation();
      selectDeckAndPromptReady(deck);
    };

    elements.decksContainer.appendChild(card);
  });
}

// --- PREPARE ROUND ---
function selectDeckAndPromptReady(deck) {
  initAudio();
  state.currentDeck = deck;
  elements.readyDeckTitle.textContent = `${deck.icon || ''} ${deck.name}`;
  elements.readyOverlay.classList.add('active');
}

elements.readyCancelBtn.onclick = () => {
  elements.readyOverlay.classList.remove('active');
};

elements.readyStartBtn.onclick = () => {
  // Synchronous permission call for iOS
  requestIOSPermissionSync();
  elements.readyOverlay.classList.remove('active');
  requestWakeLock();
  startCountdown();
};

// --- 3-2-1 COUNTDOWN ---
function startCountdown() {
  elements.countdownScreen.classList.add('active');
  let count = 3;
  elements.countdownDigit.textContent = count;
  playCountdownBeep();

  const countTimer = setInterval(() => {
    count--;
    if (count > 0) {
      elements.countdownDigit.textContent = count;
      playCountdownBeep();
    } else {
      clearInterval(countTimer);
      elements.countdownScreen.classList.remove('active');
      startRound();
    }
  }, 1000);
}

// --- WORD SHUFFLING & QUEUE ---
function shuffleWords(words) {
  const arr = [...words];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// --- ACTIVE ROUND ---
function startRound() {
  state.isPlaying = true;
  state.isLocked = false;
  state.motionState = 'NEUTRAL';
  state.score = 0;
  state.correctWords = [];
  state.passedWords = [];
  state.timeLeft = state.roundDuration;
  state.wordsQueue = shuffleWords(state.currentDeck.words);
  state.currentWordIndex = 0;

  elements.gameDeckName.textContent = state.currentDeck.name;
  elements.gameScoreDisplay.textContent = `0 pts`;
  elements.gameTimerDisplay.textContent = state.timeLeft;
  elements.gameTimerDisplay.classList.remove('urgent');

  // Reset live tilt badge
  elements.gameTiltBadge.className = 'game-tilt-indicator';
  elements.gameTiltText.textContent = 'Upright';

  elements.gameplayView.classList.add('active');
  displayCurrentWord();
  playStartChime();

  // Start countdown timer
  state.timerInterval = setInterval(() => {
    state.timeLeft--;
    elements.gameTimerDisplay.textContent = state.timeLeft;

    if (state.timeLeft <= 10) {
      elements.gameTimerDisplay.classList.add('urgent');
      if (state.timeLeft <= 5 && state.timeLeft > 0) {
        playCountdownBeep();
      }
    }

    if (state.timeLeft <= 0) {
      endRound();
    }
  }, 1000);
}

function displayCurrentWord() {
  if (state.currentWordIndex >= state.wordsQueue.length) {
    state.wordsQueue = shuffleWords(state.currentDeck.words);
    state.currentWordIndex = 0;
  }

  const item = state.wordsQueue[state.currentWordIndex];
  if (typeof item === 'string') {
    elements.currentWordText.textContent = item;
    elements.currentWordHint.textContent = '';
  } else {
    elements.currentWordText.textContent = item.word || '';
    elements.currentWordHint.textContent = item.hint || '';
  }
}

// --- GAME ACTIONS: CORRECT / PASS ---
function registerCorrect() {
  if (!state.isPlaying || state.isLocked) return;
  state.isLocked = true;

  const wordObj = state.wordsQueue[state.currentWordIndex];
  state.correctWords.push(typeof wordObj === 'string' ? wordObj : wordObj.word);
  state.score++;
  elements.gameScoreDisplay.textContent = `${state.score} pts`;

  // Flash UI
  elements.actionFlash.textContent = 'CORRECT! +1';
  elements.actionFlash.className = 'action-flash correct';
  playCorrectSound();
  triggerHaptic('correct');

  setTimeout(() => {
    elements.actionFlash.className = 'action-flash';
    state.currentWordIndex++;
    displayCurrentWord();
    // Allow next guess after quick return to neutral
    setTimeout(() => {
      state.isLocked = false;
    }, 400);
  }, 450);
}

function registerPass() {
  if (!state.isPlaying || state.isLocked) return;
  state.isLocked = true;

  const wordObj = state.wordsQueue[state.currentWordIndex];
  state.passedWords.push(typeof wordObj === 'string' ? wordObj : wordObj.word);

  // Flash UI
  elements.actionFlash.textContent = 'PASS!';
  elements.actionFlash.className = 'action-flash pass';
  playPassSound();
  triggerHaptic('pass');

  setTimeout(() => {
    elements.actionFlash.className = 'action-flash';
    state.currentWordIndex++;
    displayCurrentWord();
    setTimeout(() => {
      state.isLocked = false;
    }, 400);
  }, 450);
}

// --- ROUND FINISH ---
function endRound() {
  state.isPlaying = false;
  clearInterval(state.timerInterval);
  releaseWakeLock();
  playGameOverSound();

  elements.gameplayView.classList.remove('active');
  elements.finalScoreVal.textContent = state.score;
  elements.resultsDeckName.textContent = `Deck: ${state.currentDeck.name}`;

  // Populate results breakdown
  elements.resultsWordList.innerHTML = '';
  state.correctWords.forEach(word => {
    const row = document.createElement('div');
    row.className = 'result-row correct-row';
    row.innerHTML = `<span>🟢 ${word}</span><span>+1 pt</span>`;
    elements.resultsWordList.appendChild(row);
  });

  state.passedWords.forEach(word => {
    const row = document.createElement('div');
    row.className = 'result-row pass-row';
    row.innerHTML = `<span>🟡 ${word}</span><span>Passed</span>`;
    elements.resultsWordList.appendChild(row);
  });

  elements.resultsScreen.classList.add('active');
}

elements.resultsReplayBtn.onclick = () => {
  elements.resultsScreen.classList.remove('active');
  selectDeckAndPromptReady(state.currentDeck);
};

elements.resultsLobbyBtn.onclick = () => {
  elements.resultsScreen.classList.remove('active');
};

elements.gameQuitBtn.onclick = () => {
  if (confirm("End this round early?")) {
    endRound();
  }
};

// --- TOUCH & KEYBOARD CONTROLS ---
elements.touchPassZone.onclick = (e) => {
  e.stopPropagation();
  registerPass();
};

elements.touchCorrectZone.onclick = (e) => {
  e.stopPropagation();
  registerCorrect();
};

window.addEventListener('keydown', (e) => {
  if (!state.isPlaying) return;
  if (e.key === 'ArrowUp' || e.key === ' ') {
    registerCorrect();
  } else if (e.key === 'ArrowDown' || e.key === 'Enter') {
    registerPass();
  }
});

// =========================================================================
// --- ROCK-SOLID MOTION ENGINE (ACCELERATION GRAVITY + ORIENTATION) ---
// =========================================================================

/**
 * Evaluates current tilt gesture based on device sensors.
 *
 * Physics when phone is held against forehead in LANDSCAPE with screen facing OUT:
 * - Upright neutral: Screen is vertical. Normal to screen (Z-axis) is horizontal. Gravity along Z is ~0.
 * - Tilt Back / Face Up (looking at ceiling):
 *   Screen faces ceiling.
 *   On iOS Safari: gravity pulls into back of phone => z < -3.2 m/s²
 *   On Android: gravity pulls towards screen => z > +3.2 m/s²
 * - Tilt Forward / Face Down (nodding at floor):
 *   Screen faces floor.
 *   On iOS Safari: gravity pulls out through glass => z > +3.2 m/s²
 *   On Android: gravity pulls away from glass => z < -3.2 m/s²
 */
function getThresholds() {
  if (state.settings.sensitivity === 'high') {
    return { threshold: 4.8 };
  }
  if (state.settings.sensitivity === 'low') {
    return { threshold: 6.8 };
  }
  // Default: |Z| > 5.5 m/s² required for tilt; everything |Z| <= 5.5 is Neutral
  return { threshold: 5.5 };
}

function evaluateGestureFromGravity(z) {
  const { threshold } = getThresholds();
  let rawGesture = 'NEUTRAL';

  if (isIOS) {
    if (z < -threshold) {
      rawGesture = 'UP'; // Tilt Back / Look Up -> Correct
    } else if (z > threshold) {
      rawGesture = 'DOWN'; // Tilt Forward / Nod Down -> Pass
    } else {
      rawGesture = 'NEUTRAL'; // Everything |z| <= 5.5 is Neutral!
    }
  } else {
    // Android coordinate sign convention
    if (z > threshold) {
      rawGesture = 'UP';
    } else if (z < -threshold) {
      rawGesture = 'DOWN';
    } else {
      rawGesture = 'NEUTRAL';
    }
  }

  // Handle invert toggle in settings
  if (state.settings.invertTilt) {
    if (rawGesture === 'UP') return 'DOWN';
    if (rawGesture === 'DOWN') return 'UP';
  }

  return rawGesture;
}

// 1. PRIMARY SENSOR: Device Motion (accelerationIncludingGravity)
window.addEventListener('devicemotion', (event) => {
  const acc = event.accelerationIncludingGravity;
  if (!acc || acc.z === null || acc.z === undefined) return;

  state.permissionGranted = true;
  state.sensorData.source = 'motion';
  state.sensorData.accZ = acc.z;
  state.sensorData.accX = acc.x || 0;
  state.sensorData.accY = acc.y || 0;

  const gesture = evaluateGestureFromGravity(acc.z);
  state.sensorData.currentGesture = gesture;

  handleMotionUpdate(gesture, `Z: ${acc.z.toFixed(1)} m/s²`);
});

// 2. SECONDARY SENSOR: Device Orientation (Fallback if devicemotion is empty)
window.addEventListener('deviceorientation', (event) => {
  if (event.beta === null && event.gamma === null) return;

  state.permissionGranted = true;
  state.sensorData.beta = event.beta || 0;
  state.sensorData.gamma = event.gamma || 0;

  // Only use orientation if devicemotion is not providing values
  if (state.sensorData.source !== 'motion') {
    state.sensorData.source = 'orientation';
    // Fallback estimation using beta and gamma
    let effectivePitch = event.beta || 0;
    let gesture = 'NEUTRAL';

    // In landscape against forehead
    if (Math.abs(event.gamma || 0) > 40) {
      effectivePitch = event.gamma;
    }

    if (effectivePitch < -35) {
      gesture = state.settings.invertTilt ? 'DOWN' : 'UP';
    } else if (effectivePitch > 35) {
      gesture = state.settings.invertTilt ? 'UP' : 'DOWN';
    } else if (Math.abs(effectivePitch) < 20) {
      gesture = 'NEUTRAL';
    }

    state.sensorData.currentGesture = gesture;
    handleMotionUpdate(gesture, `Pitch: ${Math.round(effectivePitch)}°`);
  }
});

/**
 * Processes live gesture changes for both calibration test and gameplay state machine
 */
function handleMotionUpdate(gesture, rawInfoStr) {
  // 1. Update Tilt Test Modal if open
  if (elements.sensorModal.classList.contains('open')) {
    elements.testSensorRaw.textContent = `${rawInfoStr} | Mode: ${state.sensorData.source}`;

    if (gesture === 'UP') {
      elements.testTiltStatus.textContent = '🟢 TILT UP (Correct)';
      elements.testTiltStatus.className = 'gauge-status status-up';
    } else if (gesture === 'DOWN') {
      elements.testTiltStatus.textContent = '🟡 TILT DOWN (Pass)';
      elements.testTiltStatus.className = 'gauge-status status-down';
    } else {
      elements.testTiltStatus.textContent = '⚪ NEUTRAL (Upright)';
      elements.testTiltStatus.className = 'gauge-status status-neutral';
    }
  }

  // 2. Update Live Gameplay Badge
  if (state.isPlaying) {
    if (gesture === 'UP') {
      elements.gameTiltBadge.className = 'game-tilt-indicator tilt-up';
      elements.gameTiltText.textContent = 'Tilt Up 🟢';
    } else if (gesture === 'DOWN') {
      elements.gameTiltBadge.className = 'game-tilt-indicator tilt-down';
      elements.gameTiltText.textContent = 'Tilt Down 🟡';
    } else {
      elements.gameTiltBadge.className = 'game-tilt-indicator';
      elements.gameTiltText.textContent = 'Upright';
    }
  }

  // 3. Gameplay State Machine with Hysteresis Debouncing
  if (!state.isPlaying || state.isLocked) return;

  if (gesture === 'UP') {
    if (state.motionState === 'NEUTRAL') {
      state.motionState = 'UP';
      registerCorrect();
    }
  } else if (gesture === 'DOWN') {
    if (state.motionState === 'NEUTRAL') {
      state.motionState = 'DOWN';
      registerPass();
    }
  } else if (gesture === 'NEUTRAL') {
    state.motionState = 'NEUTRAL';
  }
}

// --- UI TAB NAVIGATION ---
elements.tabBtns.forEach(btn => {
  btn.onclick = () => {
    elements.tabBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    state.activeTab = btn.getAttribute('data-tab');
    renderDecks();
  };
});

// --- ROUND TIMER PILLS ---
elements.timerPills.querySelectorAll('.pill-option').forEach(pill => {
  pill.onclick = () => {
    elements.timerPills.querySelectorAll('.pill-option').forEach(p => p.classList.remove('active'));
    pill.classList.add('active');
    state.roundDuration = parseInt(pill.getAttribute('data-time'), 10);
  };
});

// --- MODALS HELPER ---
function openModal(id) {
  document.getElementById(id).classList.add('open');
  if (id === 'sensor-modal') {
    updatePermissionUI();
  }
}

function closeModal(id) {
  document.getElementById(id).classList.remove('open');
}

document.querySelectorAll('.close-btn, [data-close]').forEach(btn => {
  btn.onclick = () => {
    const target = btn.getAttribute('data-close') || btn.closest('.modal-overlay').id;
    closeModal(target);
  };
});

// --- HEADER BUTTONS ---
elements.soundBtn.onclick = () => {
  state.settings.sound = !state.settings.sound;
  elements.soundBtn.textContent = state.settings.sound ? '🔊' : '🔇';
  showToast(state.settings.sound ? 'Sound FX Enabled' : 'Sound FX Muted');
};

elements.sensorTestBtn.onclick = () => {
  requestIOSPermissionSync();
  openModal('sensor-modal');
};

elements.settingsBtn.onclick = () => {
  elements.settingSoundToggle.checked = state.settings.sound;
  elements.settingVibrateToggle.checked = state.settings.vibration;
  elements.settingInvertToggle.checked = state.settings.invertTilt;
  if (elements.settingSensitivitySelect) {
    elements.settingSensitivitySelect.value = state.settings.sensitivity;
  }
  elements.settingTouchToggle.checked = state.settings.touchEnabled;
  openModal('settings-modal');
};

// --- SETTINGS TOGGLES ---
elements.settingSoundToggle.onchange = (e) => {
  state.settings.sound = e.target.checked;
  elements.soundBtn.textContent = state.settings.sound ? '🔊' : '🔇';
};

elements.settingVibrateToggle.onchange = (e) => {
  state.settings.vibration = e.target.checked;
};

elements.settingInvertToggle.onchange = (e) => {
  state.settings.invertTilt = e.target.checked;
  showToast(e.target.checked ? 'Tilt Direction Inverted' : 'Default Tilt Restored');
};

if (elements.settingSensitivitySelect) {
  elements.settingSensitivitySelect.onchange = (e) => {
    state.settings.sensitivity = e.target.value;
    try {
      localStorage.setItem('headsup_sensitivity', e.target.value);
    } catch (err) {}
    showToast(`Tilt Sensitivity: ${e.target.value.toUpperCase()}`);
  };
}

elements.settingTouchToggle.onchange = (e) => {
  state.settings.touchEnabled = e.target.checked;
  elements.touchPassZone.style.display = e.target.checked ? 'flex' : 'none';
  elements.touchCorrectZone.style.display = e.target.checked ? 'flex' : 'none';
};

// --- CUSTOM DECK FORM SUBMISSION ---
elements.customDeckForm.onsubmit = (e) => {
  e.preventDefault();
  const name = document.getElementById('custom-deck-name').value.trim();
  const icon = document.getElementById('custom-deck-icon').value.trim() || '🎉';
  const rawWords = document.getElementById('custom-deck-words').value.trim();

  const words = rawWords.split('\n')
    .map(w => w.trim())
    .filter(w => w.length > 0)
    .map(w => ({ word: w, hint: '' }));

  if (words.length < 3) {
    alert('Please enter at least 3 words.');
    return;
  }

  const newDeck = {
    id: `custom-${Date.now()}`,
    name,
    icon,
    color: '#8b5cf6',
    description: `Custom player deck with ${words.length} words`,
    words
  };

  state.customDecks.unshift(newDeck);
  saveCustomDecks();
  closeModal('custom-modal');
  elements.customDeckForm.reset();
  showToast(`Deck "${name}" saved! 🎉`);

  // Switch to custom tab and render
  state.activeTab = 'custom';
  elements.tabBtns.forEach(b => {
    b.classList.toggle('active', b.getAttribute('data-tab') === 'custom');
  });
  renderDecks();
};

// --- INITIALIZE APP ---
function init() {
  loadCustomDecks();
  renderDecks();
  updatePermissionUI();
  try {
    const savedSens = localStorage.getItem('headsup_sensitivity');
    if (savedSens) {
      state.settings.sensitivity = savedSens;
    }
  } catch (e) {}
}

init();
