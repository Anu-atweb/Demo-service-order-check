from datetime import datetime, timezone

from .events import event_bus


def place_order(order: dict) -> dict:
    order["status"] = "placed"
    order["placed_at"] = datetime.now(timezone.utc).isoformat()
    event_bus.publish("order.placed", order)

    order["status"] = "confirmed"
    order["confirmed_at"] = datetime.now(timezone.utc).isoformat()
    event_bus.publish("order.confirmed", order)

    return order
