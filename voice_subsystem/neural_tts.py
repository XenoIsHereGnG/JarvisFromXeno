import edge_tts
from pathlib import Path

VOICE = "it-IT-GiuseppeNeural"

async def generate_speech_file(text: str, output_path: Path) -> bool:
    clean_text = text.replace("*", "").replace("`", "").strip()
    if not clean_text:
        return False
    comm = edge_tts.Communicate(clean_text, VOICE, rate="+3%", pitch="-3Hz")
    await comm.save(str(output_path))
    return True
