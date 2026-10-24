import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).parent / "jarvis_memory.db"

def init_db():
    schema = (Path(__file__).parent / "schema.sql").read_text()
    with sqlite3.connect(DB_FILE) as conn:
        conn.executescript(schema)

def get_graph_nodes(limit: int = 30) -> list:
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, category, content FROM memories ORDER BY id DESC LIMIT ?", (limit,))
        return [{"id": r[0], "category": r[1], "content": r[2]} for r in cur.fetchall()]
