import subprocess

def launch_app_native(app_name: str) -> str:
    """Apre qualsiasi applicazione su Windows 11 tramite powershell bridge."""
    try:
        res = subprocess.run(
            ["powershell", "-ExecutionPolicy", "Bypass", "-File", "os_bridge/app_launcher.ps1", "-AppName", app_name],
            capture_output=True, text=True, timeout=8
        )
        return res.stdout.strip()
    except Exception as e:
        return f"Errore apertura: {str(e)}"

def terminate_task_native(task_name: str) -> str:
    """Termina forzatamente un processo tramite PowerShell."""
    try:
        res = subprocess.run(
            ["powershell", "-ExecutionPolicy", "Bypass", "-File", "os_bridge/process_killer.ps1", "-ProcessName", task_name],
            capture_output=True, text=True, timeout=8
        )
        return res.stdout.strip()
    except Exception as e:
        return f"Errore chiusura: {str(e)}"
