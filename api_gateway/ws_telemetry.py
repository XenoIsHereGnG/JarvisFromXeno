import asyncio
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from telemetry_daemon.cpu_sampler import get_cpu_sample
from telemetry_daemon.ram_allocator import get_ram_sample
from telemetry_daemon.disk_sentry import get_disk_sample
from memory_graph.graph_engine import get_graph_nodes

router = APIRouter()

@router.websocket("/ws/telemetry")
async def telemetry_stream(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            payload = {
                "cpu": get_cpu_sample(),
                "ram": get_ram_sample(),
                "disk": get_disk_sample(),
                "nodes": get_graph_nodes(15)
            }
            await ws.send_json(payload)
            await asyncio.sleep(1.0)
    except WebSocketDisconnect:
        pass
