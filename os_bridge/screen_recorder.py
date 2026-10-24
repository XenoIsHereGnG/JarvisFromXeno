import os
import pyautogui

def capture_screen_native() -> str:
    """Cattura lo schermo del PC e salva l'immagine nei Documenti."""
    output_path = os.path.expanduser("~/Pictures/jarvis_screen.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(output_path)
    return f"Screenshot acquisito in {output_path}"
