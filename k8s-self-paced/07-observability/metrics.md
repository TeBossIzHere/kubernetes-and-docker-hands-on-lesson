# Metrics Guide

## Expose /metrics Endpoint

Add a text-based endpoint for lightweight metrics:

- total requests
- app health
- dependency status

### Example Output

```text
app_requests_total 42
app_up 1
redis_up 1
```

## Prometheus Concept

Prometheus scrapes `/metrics` periodically and stores time-series data for alerting and dashboards.
