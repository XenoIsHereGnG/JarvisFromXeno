import psutil

def get_ram_sample() -> dict:
    mem = psutil.virtual_memory()
    return {
        "used_gb": round(mem.used / (1024**3), 2),
        "total_gb": round(mem.total / (1024**3), 2),
        "percent": round(mem.percent)
    }
