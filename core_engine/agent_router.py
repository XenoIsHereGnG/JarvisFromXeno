from core_engine.gemini_client import GeminiCoreClient
from os_bridge.window_controller import launch_app_native, terminate_task_native
from os_bridge.screen_recorder import capture_screen_native

class AgentRouter:
    def __init__(self):
        self.client = GeminiCoreClient()
        self.system_prompt = (
            "Sei J.A.R.V.I.S., il sistema operativo di comando del computer. "
            "Rispondi con tono autorevole, da adulto professionista. Esegui direttamente i comandi richiesti."
        )

    def route_directive(self, prompt_text: str) -> str:
        tools = [launch_app_native, terminate_task_native, capture_screen_native]
        response = self.client.execute_prompt(self.system_prompt, prompt_text, tools)
        return response.text if response.text else "Direttiva eseguita con successo, Comandante."
