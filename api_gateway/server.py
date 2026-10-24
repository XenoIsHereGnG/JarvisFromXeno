from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from pathlib import Path
from api_gateway.ws_telemetry import router as telemetry_router
from api_gateway.ws_command import router as command_router, agent_instance
from voice_subsystem.neural_tts import generate_speech_file
from memory_graph.graph_engine import init_db

app = FastAPI(title="JARVIS Enterprise OS")
init_db()

BASE_DIR = Path(__file__).resolve().parent.parent
UI_DIR = BASE_DIR / "ui_layout"
CONTROLLERS_DIR = BASE_DIR / "ui_controllers"
NEURAL_DIR = BASE_DIR / "neural_network"
ENV_FILE = BASE_DIR / ".env"

app.mount("/ui_layout", StaticFiles(directory=UI_DIR), name="ui_layout")
app.mount("/ui_controllers", StaticFiles(directory=CONTROLLERS_DIR), name="ui_controllers")
app.mount("/neural_network", StaticFiles(directory=NEURAL_DIR), name="neural_network")

app.include_router(telemetry_router)
app.include_router(command_router)

MASTER_PASSWORD = "PASSWORDCHANGED12$"

class PasswordPayload(BaseModel):
    password: str

class ApiKeyPayload(BaseModel):
    api_key: str

@app.post("/api/auth/verify-password")
async def verify_password(data: PasswordPayload):
    audio_dest = UI_DIR / "speech.mp3"
    if data.password == MASTER_PASSWORD:
        await generate_speech_file("Crittografia verificata. Benvenuto nel centro di comando, Signore. Inserire la chiave neurale Gemini per inizializzare i nuclei.", audio_dest)
        return {"authenticated": True, "has_audio": True}
    else:
        await generate_speech_file("Accesso negato. Violazione di sicurezza rilevata.", audio_dest)
        return JSONResponse({"authenticated": False, "has_audio": True}, status_code=401)

@app.post("/api/auth/set-api-key")
async def set_api_key(data: ApiKeyPayload):
    key = data.api_key.strip()
    if len(key) < 15:
        return JSONResponse({"status": "invalid", "msg": "Chiave API troppo corta o non valida."}, status_code=400)
    
    # Aggiorna il motore live e salva nel .env
    agent_instance.set_api_key(key)
    ENV_FILE.write_text(f"GEMINI_API_KEY={key}\nJARVIS_VOICE=it-IT-GiuseppeNeural\n", encoding="utf-8")
    
    audio_dest = UI_DIR / "speech.mp3"
    await generate_speech_file("Connessione con la matrice Gemini stabilita. Tutti i sistemi neurali e i controlli del computer sono operativi.", audio_dest)
    return {"status": "ok", "has_audio": True}

@app.get("/")
def get_dashboard():
    return FileResponse(UI_DIR / "index.html")
