class STTReceiver:
    def __init__(self):
        self.is_active = True

    def process_incoming_stream(self, chunk: bytes) -> str:
        # Buffer di ricezione stream binario da WebRTC / WebSocket
        return "Chunk audio ricevuto e sincronizzato."
