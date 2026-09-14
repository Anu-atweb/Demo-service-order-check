from . import fraud_check_service  # noqa: F401  (registers event subscribers)
from . import notification_service  # noqa: F401  (registers event subscribers)
from .order_service import place_order


def main() -> None:
    order = {"id": "ORD-1001", "customer_email": "customer@example.com", "total_cents": 4599}
    place_order(order)


if __name__ == "__main__":
    main()
