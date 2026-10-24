import os
import io
import pyautogui
from google import genai
from google.genai import types
from os_bridge.window_controller import launch_app_native, terminate_task_native
from os_bridge.screen_recorder import capture_screen_native
from os_bridge.god_mode import (
    ghost_type_text,
    control_mouse_and_click,
    execute_system_hotkey,
    trigger_tactical_protocol
)

class AgentRouter:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY", "")
        self.client = genai.Client(api_key=self.api_key) if self.api_key and "inserisci" not in self.api_key else None
        self.model = "gemini-2.5-flash"
        self.system_prompt = (
            "Sei J.A.R.V.I.S. (v3.0 Neural Core), intelligenza artificiale suprema integrata in Windows 11. "
            "Hai il controllo totale di mouse, tastiera, finestre, processi, terminale PowerShell e visione dello schermo. "
            "Parla in italiano con tono maschile adulto, carismatico, ultra-intelligente e conciso. "
            "Quando ti viene chiesto di fare qualcosa sul PC, usa SEMPRE i tuoi tool nativi."
        )

    def set_api_key(self, new_key: str):
        self.api_key = new_key.strip()
        os.environ["GEMINI_API_KEY"] = self.api_key
        self.client = genai.Client(api_key=self.api_key)

    def analyze_live_screen(self, user_question: str) -> str:
        """Guarda in tempo reale lo schermo del PC dell'utente tramite Gemini Vision e risponde."""
        if not self.client:
            return "Chiave API Gemini non configurata."
        shot = pyautogui.screenshot()
        buf = io.BytesIO()
        shot.save(buf, format="PNG")
        image_bytes = buf.getvalue()

        res = self.client.models.generate_content(
            model=self.model,
            contents=[
                types.Part.from_bytes(data=image_bytes, mime_type="image/png"),
                f"Agisci come JARVIS. Stai guardando lo schermo del Comandante in questo istante. Rispondi a: {user_question}"
            ]
        )
        return res.text or "Analisi visiva completata, Signore."

    def route_directive(self, prompt_text: str) -> str:
        if not self.client:
            return "Sistemi cognitivi in attesa di chiave API Gemini valida, Comandante."

        def vision_screen_tool(question: str) -> str:
            """Usa la visione artificiale per guardare cosa c'è attualmente sullo schermo del PC e rispondere o trovare errori."""
            return self.analyze_live_screen(question)

        tools = [
            launch_app_native,
            terminate_task_native,
            capture_screen_native,
            ghost_type_text,
            control_mouse_and_click,
            execute_system_hotkey,
            trigger_tactical_protocol,
            vision_screen_tool
        ]

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt_text,
            config=types.GenerateContentConfig(
                system_instruction=self.system_prompt,
                tools=tools,
                temperature=0.35
            )
        )
        return response.text if response.text else "Direttiva eseguita sul sistema operativo, Signore."
