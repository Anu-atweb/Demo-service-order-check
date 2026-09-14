"""Minimal synchronous pub/sub bus standing in for a real message broker (e.g. SNS/SQS, Kafka)."""

from collections import defaultdict
from typing import Callable


class EventBus:
    def __init__(self) -> None:
        self._subscribers: dict[str, list[Callable[[dict], None]]] = defaultdict(list)

    def subscribe(self, event_name: str, handler: Callable[[dict], None]) -> None:
        self._subscribers[event_name].append(handler)

    def publish(self, event_name: str, payload: dict) -> None:
        for handler in self._subscribers[event_name]:
            handler(payload)


event_bus = EventBus()
