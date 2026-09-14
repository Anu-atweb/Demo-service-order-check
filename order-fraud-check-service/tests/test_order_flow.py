from app import fraud_check_service  # noqa: F401
from app import notification_service  # noqa: F401
from app.order_service import place_order


def test_place_order_confirms_and_sets_timestamps():
    order = {"id": "ORD-TEST-1"}
    result = place_order(order)

    assert result["status"] == "confirmed"
    assert "placed_at" in result
    assert "confirmed_at" in result


def test_confirmation_email_is_scheduled_not_sent_immediately(monkeypatch):
    scheduled = {}

    def fake_timer(delay_seconds, func, args):
        scheduled["delay_seconds"] = delay_seconds
        scheduled["order"] = args[0]

        class _NoOpTimer:
            daemon = False

            def start(self):
                pass

        return _NoOpTimer()

    monkeypatch.setattr(notification_service.threading, "Timer", fake_timer)

    order = {"id": "ORD-TEST-2"}
    place_order(order)

    assert scheduled["delay_seconds"] == notification_service.CONFIRMATION_EMAIL_DELAY_SECONDS
    assert scheduled["order"]["id"] == "ORD-TEST-2"
