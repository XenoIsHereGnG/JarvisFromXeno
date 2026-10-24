from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from api_gateway.ws_telemetry import router as telemetry_router
from api_gateway.ws_command import router as command_router
from memory_graph.graph_engine import init_db

app = FastAPI(title="JARVIS OS Gateway")
init_db()

UI_DIR = Path(__file__).resolve().parent.parent / "ui_layout"
CONTROLLERS_DIR = Path(__file__).resolve().parent.parent / "ui_controllers"

app.mount("/ui_layout", StaticFiles(directory=UI_DIR), name="ui_layout")
app.mount("/ui_controllers", StaticFiles(directory=CONTROLLERS_DIR), name="ui_controllers")

app.include_router(telemetry_router)
app.include_router(command_router)

@app.get("/")
def get_dashboard():
    return FileResponse(UI_DIR / "index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_gateway.server:app", host="127.0.0.1", port=8000, reload=True)
