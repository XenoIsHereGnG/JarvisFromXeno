import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

class GeminiCoreClient:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY assente nelle variabili d'ambiente.")
        self.client = genai.Client(api_key=self.api_key)
        self.model = "gemini-2.5-flash"

    def execute_prompt(self, system_instruction: str, contents: str, tools: list):
        return self.client.models.generate_content(
            model=self.model,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                tools=tools,
                temperature=0.3
            )
        )
