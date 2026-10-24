# Verifica rapida latenza CPU e memoria allocata
$Metric = Get-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize, FreePhysicalMemory
Write-Host "Diagnostica Memoria: $($Metric.FreePhysicalMemory / 1MB) GB liberi su $($Metric.TotalVisibleMemorySize / 1MB) GB totali." -ForegroundColor Green
