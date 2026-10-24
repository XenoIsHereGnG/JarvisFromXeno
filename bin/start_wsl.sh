#!/usr/bin/env bash
# Avvio di JARVIS in ambiente Bash/WSL2
set -e
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
echo "Avvio Core JARVIS da: $PROJECT_ROOT"
source "$PROJECT_ROOT/venv/bin/activate" 2>/dev/null || true
python3 "$PROJECT_ROOT/api_gateway/server.py"
