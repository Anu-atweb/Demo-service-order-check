import threading

from .events import event_bus

# ADR-001: hold the confirmation email so the fraud check pipeline has a window
# to flag/cancel the order before the customer is notified.
CONFIRMATION_EMAIL_DELAY_SECONDS = 5 * 60


def send_confirmation_email(order: dict) -> None:
    print(f"[notification] sending order confirmation email for order {order['id']}")


def schedule_confirmation_email(order: dict) -> None:
    timer = threading.Timer(CONFIRMATION_EMAIL_DELAY_SECONDS, send_confirmation_email, args=(order,))
    timer.daemon = True
    timer.start()


event_bus.subscribe("order.confirmed", schedule_confirmation_email)
