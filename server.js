const http = require('http');
const https = require('https');
const fs = require('fs');
const path = require('path');
const os = require('os');
const url = require('url');

const PORT = process.env.PORT || 9876;
const PUBLIC_DIR = __dirname;

const MIME_TYPES = {
  '.html': 'text/html; charset=UTF-8',
  '.js': 'application/javascript; charset=UTF-8',
  '.css': 'text/css; charset=UTF-8',
  '.json': 'application/json; charset=UTF-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon'
};

const GAMEGAL_CATALOG = {
  pictionary: {
    id: 2,
    name: "Pictionary",
    categories: [
      { id: 6, name: "Easy" },
      { id: 7, name: "Medium" },
      { id: 8, name: "Hard" },
      { id: 9, name: "Really Hard" }
    ]
  },
  catchphrase: {
    id: 3,
    name: "Catchphrase",
    categories: [
      { id: 13, name: "Easy" },
      { id: 14, name: "Medium" },
      { id: 15, name: "Hard" }
    ]
  },
  holidays: {
    id: 4,
    name: "Western Holidays",
    categories: [
      { id: 45, name: "Valentine's Day" },
      { id: 23, name: "Fourth of July" },
      { id: 24, name: "Halloween" },
      { id: 29, name: "Thanksgiving" },
      { id: 30, name: "Christmas" },
      { id: 31, name: "Christmas Songs" },
      { id: 37, name: "New Year's" },
      { id: 35, name: "Spring / Easter" },
      { id: 39, name: "Summer" },
      { id: 40, name: "Fall / Autumn" },
      { id: 38, name: "Winter" },
      { id: 44, name: "Summer Olympics" }
    ]
  },
  charades: {
    id: 5,
    name: "Charades & Actions",
    categories: [
      { id: 36, name: "Actions" },
      { id: 25, name: "Easy" },
      { id: 26, name: "Medium" },
      { id: 27, name: "Hard" },
      { id: 28, name: "Really Hard" }
    ]
  },
  subjects: {
    id: 1,
    name: "Subjects & Themes",
    categories: [
      { id: 1, name: "Animals" },
      { id: 56, name: "Common Animals" },
      { id: 4, name: "Places" },
      { id: 65, name: "Sports" },
      { id: 2, name: "Food and Cooking" },
      { id: 63, name: "Nature" },
      { id: 52, name: "Around the House" },
      { id: 66, name: "Travel" },
      { id: 59, name: "Feelings and Emotions" }
    ]
  },
  wordplay: {
    id: 7,
    name: "Wordplay",
    categories: [
      { id: 69, name: "Idioms and Sayings" },
      { id: 71, name: "Opposites" },
      { id: 72, name: "Pairs" }
    ]
  },
  movies: {
    id: 8,
    name: "Movies",
    categories: [
      { id: 82, name: "Disney and Pixar Movies" },
      { id: 80, name: "Animated Movies" },
      { id: 81, name: "Comedies" },
      { id: 84, name: "Family Movies" },
      { id: 90, name: "Sci-Fi Movies" },
      { id: 76, name: "All Movies" }
    ]
  },
  individuals: {
    id: 9,
    name: "Famous People",
    categories: [
      { id: 92, name: "Celebrities" },
      { id: 93, name: "Characters" },
      { id: 94, name: "Historical People" }
    ]
  }
};

function cleanWord(str) {
  if (!str) return '';
  return str.replace(/[\ufeff\u200b\u200c\u200d]/g, '')
            .replace(/Ã¯Â»Â¿/g, '')
            .replace(/ï»¿/g, '')
            .trim();
}

function fetchGameGalAPI(gameId, categoryId, callback) {
  const targetUrl = `https://www.thegamegal.com/wordgenerator/generator.php?game=${encodeURIComponent(gameId)}&category=${encodeURIComponent(categoryId)}`;
  const options = {
    headers: {
      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
      'Accept': 'application/json, text/javascript, */*'
    }
  };

  https.get(targetUrl, options, (apiRes) => {
    let data = '';
    apiRes.on('data', chunk => { data += chunk; });
    apiRes.on('end', () => {
      try {
        const parsed = JSON.parse(data);
        if (parsed.success && Array.isArray(parsed.words)) {
          const cleaned = [];
          const seen = new Set();
          for (const item of parsed.words) {
            const w = cleanWord(item);
            if (w && !seen.has(w.toLowerCase())) {
              seen.add(w.toLowerCase());
              cleaned.push(w);
            }
          }
          callback(null, cleaned);
        } else {
          callback(new Error("API returned success: false or invalid words array"));
        }
      } catch (err) {
        callback(err);
      }
    });
  }).on('error', err => {
    callback(err);
  });
}

const server = http.createServer((req, res) => {
  // CORS & Security headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  res.setHeader('Cache-Control', 'no-cache');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  const parsedUrl = url.parse(req.url, true);
  const pathname = parsedUrl.pathname;

  // --- API ROUTE: Game Gal Catalog ---
  if (pathname === '/api/gamegal/catalog') {
    res.writeHead(200, { 'Content-Type': 'application/json; charset=UTF-8' });
    res.end(JSON.stringify({ success: true, catalog: GAMEGAL_CATALOG }));
    return;
  }

  // --- API ROUTE: Game Gal Word Fetch Proxy ---
  if (pathname === '/api/gamegal') {
    const game = parsedUrl.query.game;
    const category = parsedUrl.query.category;

    if (!game || !category) {
      res.writeHead(400, { 'Content-Type': 'application/json; charset=UTF-8' });
      res.end(JSON.stringify({ success: false, error: "Missing 'game' or 'category' query parameter" }));
      return;
    }

    fetchGameGalAPI(game, category, (err, words) => {
      if (err) {
        res.writeHead(502, { 'Content-Type': 'application/json; charset=UTF-8' });
        res.end(JSON.stringify({ success: false, error: err.message }));
        return;
      }
      res.writeHead(200, { 'Content-Type': 'application/json; charset=UTF-8' });
      res.end(JSON.stringify({ success: true, game, category, count: words.length, words }));
    });
    return;
  }

  // --- STATIC FILE SERVING ---
  let reqPath = decodeURI(pathname);
  if (reqPath === '/' || reqPath === '') {
    reqPath = '/index.html';
  }

  const filePath = path.join(PUBLIC_DIR, reqPath);

  // Prevent directory traversal
  if (!filePath.startsWith(PUBLIC_DIR)) {
    res.writeHead(403, { 'Content-Type': 'text/plain' });
    res.end('403 Forbidden');
    return;
  }

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      res.end('404 Not Found');
      return;
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';

    res.writeHead(200, { 'Content-Type': contentType });
    fs.createReadStream(filePath).pipe(res);
  });
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`\n==================================================`);
  console.log(`🎮 Heads-Up Charades Game Server running on port ${PORT}`);
  console.log(`Local Access: http://localhost:${PORT}`);

  // Display LAN IPs
  const interfaces = os.networkInterfaces();
  for (const name of Object.keys(interfaces)) {
    for (const net of interfaces[name]) {
      if (net.family === 'IPv4' && !net.internal) {
        console.log(`Network Access: http://${net.address}:${PORT}`);
      }
    }
  }
  console.log(`==================================================\n`);
});
