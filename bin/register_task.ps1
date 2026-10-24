# Registra JARVIS all'accesso utente su Windows 11
$Action = New-ScheduledTaskAction -Execute 'cmd.exe' -Argument '/c bin\start_jarvis.bat' -WorkingDirectory (Get-Location).Path
$Trigger = New-ScheduledTaskTrigger -AtLogOn
Register-ScheduledTask -TaskName "JarvisCommandCenter" -Action $Action -Trigger $Trigger -Description "Avvio automatico HUD JARVIS" -RunLevel Highest -Force
Write-Host "Task JarvisCommandCenter registrato con successo." -ForegroundColor Cyan
