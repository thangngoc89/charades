#!/bin/bash
# Stop Heads-Up Charades Server and Tunnel

APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$APP_DIR" || exit 1

NODE_PID_FILE="$APP_DIR/server.pid"
TUNNEL_PID_FILE="$APP_DIR/tunnel.pid"

if [ -f "$NODE_PID_FILE" ]; then
  PID=$(cat "$NODE_PID_FILE")
  if kill -0 "$PID" 2>/dev/null; then
    kill "$PID"
    echo "Stopped web server (PID $PID)."
  fi
  rm -f "$NODE_PID_FILE"
fi

if [ -f "$TUNNEL_PID_FILE" ]; then
  PID=$(cat "$TUNNEL_PID_FILE")
  if kill -0 "$PID" 2>/dev/null; then
    kill "$PID"
    echo "Stopped tunnel (PID $PID)."
  fi
  rm -f "$TUNNEL_PID_FILE"
fi

echo "All services stopped."
