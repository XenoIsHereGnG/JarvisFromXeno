import os
import time
import subprocess
import pyautogui
import pyperclip

pyautogui.FAILSAFE = False

def ghost_type_text(text: str, press_enter: bool = True) -> str:
    """Scrive automaticamente qualsiasi testo sulla finestra attiva del PC come un fantasma."""
    time.sleep(0.8)
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
    if press_enter:
        pyautogui.press("enter")
    return f"Testo digitato automaticamente: '{text[:40]}...'"

def control_mouse_and_click(x: int, y: int, click_type: str = "single") -> str:
    """Muove fisicamente il cursore del mouse alle coordinate X, Y e clicca (single, double, right)."""
    pyautogui.moveTo(x, y, duration=0.5)
    if click_type == "double":
        pyautogui.doubleClick()
    elif click_type == "right":
        pyautogui.rightClick()
    else:
        pyautogui.click()
    return f"Cursore spostato su ({x}, {y}) con azione {click_type}."

def execute_system_hotkey(keys_csv: str) -> str:
    """Preme combinazioni di tasti su Windows (es: 'win,d' per mostrare desktop, 'ctrl,shift,esc' per task manager, 'alt,tab')."""
    keys = [k.strip().lower() for k in keys_csv.split(",")]
    pyautogui.hotkey(*keys)
    return f"Combinazione tasti eseguita: {keys}"

def trigger_tactical_protocol(protocol_name: str) -> str:
    """Attiva protocolli speciali sul PC: 'ghost' (minimizza tutto e silenzia), 'lockdown' (blocca Windows), 'overdrive' (ottimizza e pulisce temp), 'matrix'."""
    p = protocol_name.lower()
    if "lock" in p:
        subprocess.Popen("rundll32.exe user32.dll,LockWorkStation", shell=True)
        return "Protocollo Lockdown attivato: Stazione Windows bloccata."
    elif "ghost" in p or "fantasma" in p:
        pyautogui.hotkey("win", "d")
        return "Protocollo Fantasma attivo: Finestre occultate e assetto stealth impostato."
    elif "overdrive" in p:
        subprocess.run(["powershell", "-Command", "Clear-RecycleBin -Force -ErrorAction SilentlyContinue"], timeout=5)
        return "Protocollo Overdrive completato: Cestino svuotato e risorse liberate."
    return f"Protocollo '{protocol_name}' sincronizzato sull'HUD."
