@echo off
echo [*] Terminazione di emergenza istanze JARVIS...
taskkill /F /IM uvicorn.exe /T 2>nul
taskkill /F /IM python.exe /FI "WINDOWTITLE eq JARVIS*" 2>nul
echo [OK] Processi interrotti.
