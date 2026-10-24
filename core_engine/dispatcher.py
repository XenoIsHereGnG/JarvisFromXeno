import asyncio
from typing import Callable, Dict

class CommandDispatcher:
    def __init__(self):
        self._registry: Dict[str, Callable] = {}

    def register(self, command_name: str, handler: Callable):
        self._registry[command_name] = handler

    async def dispatch(self, command_name: str, *args, **kwargs):
        if command_name in self._registry:
            func = self._registry[command_name]
            return await func(*args, **kwargs) if asyncio.iscoroutinefunction(func) else func(*args, **kwargs)
        raise KeyError(f"Comando {command_name} non registrato nel dispatcher.")
