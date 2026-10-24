param([string]$AppName)
try {
    Start-Process $AppName -ErrorAction Stop
    Write-Output "OK: Applicazione $AppName avviata."
} catch {
    Write-Output "ERR: Impossibile avviare $AppName: $_"
}
