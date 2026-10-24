$cscPath = "C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe"
$sourceFile = "native_launcher\JarvisLauncher.cs"
$outputExe = "JARVIS_OS.exe"

Write-Host "[*] Compilazione nativa di JARVIS_OS.exe in corso..." -ForegroundColor Cyan
& $cscPath /target:winexe /out:$outputExe $sourceFile
Write-Host "[OK] Eseguibile creato con successo: $outputExe" -ForegroundColor Green
