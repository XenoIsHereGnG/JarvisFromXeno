import asyncio
from typing import Callable, List

class EventBus:
    def __init__(self):
        self._subscribers: List[Callable] = []

    def subscribe(self, callback: Callable):
        self._subscribers.append(callback)

    async def emit(self, event_type: str, data: dict):
        for sub in self._subscribers:
            if asyncio.iscoroutinefunction(sub):
                await sub(event_type, data)
            else:
                sub(event_type, data)
