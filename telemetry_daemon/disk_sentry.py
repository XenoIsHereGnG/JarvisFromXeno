import psutil

def get_disk_sample() -> dict:
    disk = psutil.disk_usage('C:')
    return {
        "free_gb": round(disk.free / (1024**3), 1),
        "percent": round(disk.percent)
    }
