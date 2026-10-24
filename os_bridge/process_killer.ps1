param([string]$ProcessName)
Stop-Process -Name $ProcessName -Force -ErrorAction SilentlyContinue
Write-Output "Processo $ProcessName terminato."
