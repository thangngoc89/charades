# 📱 Heads Up! Charades Web Game

A mobile-first party charades game designed to be played with **Kids under 10** or **Millennials**, featuring real gyroscope tilt motion detection, audio effects, haptics, and custom deck support.

---

## 🌐 Live Access Portal

- **HTTPS Mobile Portal**: [https://shots-victory-expired-italia.trycloudflare.com](https://shots-victory-expired-italia.trycloudflare.com)
- **Local Access**: `http://localhost:9876`

> **Note**: Both the Node.js server and Cloudflare HTTPS tunnel run in detached background sessions (`setsid`) and will **remain active even after the CLI session ends**.

---

## 🎮 How to Play

1. **Open the Portal URL** on your mobile phone browser (Safari, Chrome, etc.).
2. **Select an Age Category**:
   - 🧒 **Kids (<10)**: *Zoo & Animals*, *Disney & Cartoons*, *Silly Actions*, *Yummy Treats*.
   - 🥑 **Millennials**: *90s & 2000s Nostalgia*, *Iconic TV & Movies*, *Adulting & Struggles*, *90s & 2000s Bangers*.
   - ✏️ **Custom Decks**: Create and save your own decks directly in the app!
3. **Choose Round Duration**: 45s, 60s (default), 90s, or 120s.
4. Tap **Play Deck** -> **Start Round**:
   - Hold phone **horizontally on your forehead** with the screen facing your teammates.
5. **Tilt Controls**:
   - 🟢 **Tilt Back / Up (Look at ceiling)**: **CORRECT! (+1 point)**
   - 🟡 **Tilt Forward / Down (Nod down)**: **PASS (Skip to next word)**
   - ⚪ **Return to Neutral (Upright)** before making your next guess (prevents accidental skips).
6. **Touch / Click Fallback**:
   - Tap **Right side of screen**: Correct
   - Tap **Left side of screen**: Pass
   - Keyboard (Desktop testing): `Space` / `Arrow Up` = Correct, `Enter` / `Arrow Down` = Pass.

---

## 🛠️ Server Management

The server runs locally on port 9876 and is tunneled through Cloudflare for SSL/HTTPS (required by mobile browsers for device motion sensors):

- **Start server & tunnel**:
  ```bash
  bash start.sh
  ```
- **Stop server & tunnel**:
  ```bash
  bash stop.sh
  ```
- **View logs**:
  - Web Server: `cat server.log`
  - Cloudflare Tunnel: `cat tunnel.log`
