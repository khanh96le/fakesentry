import os
import random

import sentry_sdk
import time

SENTRY_DSN = os.environ.get("SENTRY_DSN")
INTERVAL_SECONDS = os.environ.get("INTERVAL_SECONDS", 5)


def send_exception_to_sentry(exception):
    sentry_sdk.capture_exception(exception)
    print(f"Simulated <{exception.__class__.__name__}> exception sent to Sentry!")


def simulate_exceptions():
    exceptions = [
        ZeroDivisionError("Division by zero"),
        ValueError("Invalid value"),
        IndexError("Index out of range"),
        FileNotFoundError("File not found"),
        KeyError("Key not found"),
    ]

    exception = random.choice(exceptions)
    try:
        raise exception
    except Exception as e:
        send_exception_to_sentry(e)
        time.sleep(INTERVAL_SECONDS)


def main():
    # Initialize Sentry SDK with your DSN
    sentry_sdk.init(SENTRY_DSN)

    # Simulate different exceptions and send them to Sentry
    while True:
        simulate_exceptions()


if __name__ == "__main__":
    main()
