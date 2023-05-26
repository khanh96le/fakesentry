# Fake sentry

Simulate sending events to your Sentry project to test if it works or not

### How to run
```bash
docker run --rm -e SENTRY_DSN=<YOUR_SENTRY_DSN> -e INTERVAL_SECONDS=5 khanhlq/fakesentry:v2
```