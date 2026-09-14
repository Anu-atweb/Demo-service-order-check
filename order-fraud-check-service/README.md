# Order Fraud Check Service (Demo)

A small mock service that models the order → confirmation → notification flow
for an e-commerce checkout, used to demonstrate the timing change described in
**ADR-001: Run Fraud Checks After Order Placement**.

## Flow

1. `order_service.place_order()` places the order and publishes `order.placed`.
2. `fraud_check_service` runs the fraud check immediately on `order.placed`,
   without blocking the checkout response.
3. `order_service` confirms the order and publishes `order.confirmed`.
4. `notification_service` sends the confirmation email, delayed by 5 minutes
   after `order.confirmed`, so the fraud pipeline has a window to flag or
   cancel the order before the customer is notified.

## Run the demo

```bash
python -m app.main
```

You'll see the fraud check log line immediately, and the confirmation email
log line ~5 minutes later (see `CONFIRMATION_EMAIL_DELAY_SECONDS` in
`app/notification_service.py` to shorten this for local testing).
