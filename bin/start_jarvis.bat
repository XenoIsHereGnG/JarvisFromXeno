@echo off
title JARVIS COMMAND CENTER BOOTSTRAP
color 0B
echo [*] Avvio dell'ambiente virtuale e del server JARVIS...
cd /d "%~dp0.."
call venv\Scripts\activate.bat
python -m uvicorn api_gateway.server:app --host 127.0.0.1 --port 8000 --reload
pause
