#!/bin/bash
# Heads-Up Charades Startup Script
# Starts Node server and Cloudflare tunnel in detached background sessions

APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$APP_DIR" || exit 1

PORT=9876
NODE_PID_FILE="$APP_DIR/server.pid"
TUNNEL_PID_FILE="$APP_DIR/tunnel.pid"

# Locate Node binary
NODE_BIN="/home/khoa/.local/share/mise/installs/node/22.12.0/bin/node"
if [ ! -x "$NODE_BIN" ]; then
  NODE_BIN=$(which node)
fi

# Stop existing if running
if [ -f "$NODE_PID_FILE" ] && kill -0 "$(cat "$NODE_PID_FILE")" 2>/dev/null; then
  echo "Stopping existing server..."
  kill "$(cat "$NODE_PID_FILE")" 2>/dev/null
  sleep 1
fi

if [ -f "$TUNNEL_PID_FILE" ] && kill -0 "$(cat "$TUNNEL_PID_FILE")" 2>/dev/null; then
  echo "Stopping existing tunnel..."
  kill "$(cat "$TUNNEL_PID_FILE")" 2>/dev/null
  sleep 1
fi

# Kill any rogue server on port 9876
fuser -k 9876/tcp 2>/dev/null

# Start Node server using setsid
echo "Starting web server on port $PORT..."
setsid "$NODE_BIN" "$APP_DIR/server.js" > "$APP_DIR/server.log" 2>&1 < /dev/null &
echo $! > "$NODE_PID_FILE"

sleep 1

# Start Cloudflare Tunnel using setsid with HTTP2
echo "Starting Cloudflare HTTPS tunnel..."
setsid cloudflared tunnel --protocol http2 --url "http://127.0.0.1:$PORT" > "$APP_DIR/tunnel.log" 2>&1 < /dev/null &
echo $! > "$TUNNEL_PID_FILE"

echo "Waiting for public HTTPS portal URL..."
URL=""
for i in {1..20}; do
  sleep 1
  URL=$(grep -o 'https://[-a-zA-Z0-9.]*\.trycloudflare\.com' "$APP_DIR/tunnel.log" | tail -n 1)
  if [ -n "$URL" ]; then
    break
  fi
done

echo ""
echo "============================================================"
echo "🎉 HEADS-UP CHARADES IS LIVE!"
echo "============================================================"
if [ -n "$URL" ]; then
  echo "📱 Mobile Portal URL (HTTPS): $URL"
  echo "$URL" > "$APP_DIR/PORTAL_URL.txt"
  echo ""
  echo "Open the URL above on your phone's browser to play!"
else
  echo "⚠️ Cloudflare tunnel took longer to assign. Check $APP_DIR/tunnel.log"
  echo "Local URL: http://localhost:$PORT"
fi
echo "============================================================"
echo "Both server and tunnel are running in detached background sessions"
echo "and will remain active even when this CLI session ends."
echo "To stop them later, run: bash stop.sh"
echo "============================================================"
