from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pathlib import Path
from core_engine.agent_router import AgentRouter
from voice_subsystem.neural_tts import generate_speech_file

router = APIRouter()
agent = AgentRouter()
AUDIO_DEST = Path(__file__).resolve().parent.parent / "ui_layout" / "speech.mp3"

@router.websocket("/ws/commands")
async def command_stream(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            data = await ws.receive_json()
            user_text = data.get("prompt", "")
            if not user_text:
                continue
            
            response_text = agent.route_directive(user_text)
            has_voice = await generate_speech_file(response_text, AUDIO_DEST)
            
            await ws.send_json({
                "response": response_text,
                "has_audio": has_voice
            })
    except WebSocketDisconnect:
        pass
