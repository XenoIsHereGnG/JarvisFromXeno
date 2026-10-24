from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pathlib import Path
from core_engine.agent_router import AgentRouter
from voice_subsystem.neural_tts import generate_speech_file
from neural_network.intent_classifier import TacticalIntentClassifier

router = APIRouter()
agent_instance = AgentRouter()
AUDIO_DEST = Path(__file__).resolve().parent.parent / "ui_layout" / "speech.mp3"

@router.websocket("/ws/commands")
async def command_stream(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            data = await ws.receive_json()
            user_text = data.get("prompt", "").strip()
            if not user_text:
                continue

            # Classificazione neurale istantanea dell'agente
            intent = TacticalIntentClassifier.classify(user_text)
            await ws.send_json({"type": "agent_activated", "intent": intent})

            # Esecuzione su Gemini + OS Tools
            response_text = agent_instance.route_directive(user_text)
            has_voice = await generate_speech_file(response_text, AUDIO_DEST)

            # Rileva se è stato attivato un cambio di tema/protocollo
            low = user_text.lower()
            protocol_mode = "optimal"
            if "red alert" in low or "allarme" in low or "lockdown" in low:
                protocol_mode = "red_alert"
            elif "ghost" in low or "fantasma" in low or "stealth" in low:
                protocol_mode = "ghost"
            elif "overdrive" in low or "massima potenza" in low:
                protocol_mode = "overdrive"

            await ws.send_json({
                "type": "final_response",
                "response": response_text,
                "has_audio": has_voice,
                "intent": intent,
                "protocol": protocol_mode
            })
    except WebSocketDisconnect:
        pass
