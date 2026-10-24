import psutil

def get_cpu_sample() -> dict:
    return {
        "overall": round(psutil.cpu_percent(interval=None)),
        "threads": psutil.cpu_percent(percpu=True),
        "freq_mhz": round(psutil.cpu_freq().current) if psutil.cpu_freq() else 1700
    }
