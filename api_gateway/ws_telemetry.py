import asyncio
import psutil
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from telemetry_daemon.cpu_sampler import get_cpu_sample
from telemetry_daemon.ram_allocator import get_ram_sample
from telemetry_daemon.disk_sentry import get_disk_sample
from memory_graph.graph_engine import get_graph_nodes
from neural_network.synapse_net import neural_engine

router = APIRouter()

@router.websocket("/ws/telemetry")
async def telemetry_stream(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            cpu = get_cpu_sample()
            ram = get_ram_sample()
            disk = get_disk_sample()
            proc_count = len(psutil.pids())

            # Forward + Backprop in tempo reale sulla Rete Neurale
            nn_state = neural_engine.forward_and_learn(
                cpu["overall"], ram["percent"], disk["percent"], proc_count
            )

            payload = {
                "cpu": cpu,
                "ram": ram,
                "disk": disk,
                "processes": proc_count,
                "neural_net": nn_state,
                "nodes": get_graph_nodes(22)
            }
            await ws.send_json(payload)
            await asyncio.sleep(0.8)
    except WebSocketDisconnect:
        pass
