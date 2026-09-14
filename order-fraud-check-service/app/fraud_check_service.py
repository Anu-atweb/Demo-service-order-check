from .events import event_bus


def run_fraud_check(order: dict) -> None:
    """Run per ADR-001: fraud checks execute immediately after order placement.

    This runs off the checkout critical path (it's an event subscriber, not part
    of the place_order() call chain the customer waits on). A real implementation
    would call the fraud scoring model/service here and, on a positive signal,
    cancel the order and cancel the pending confirmation email before it's sent.
    """
    print(f"[fraud-check] running fraud check for order {order['id']} immediately after placement")


event_bus.subscribe("order.placed", run_fraud_check)
