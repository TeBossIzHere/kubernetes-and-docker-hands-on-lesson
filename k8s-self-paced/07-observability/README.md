# 07 - Observability

## Concept
Observe app behavior using logs and metrics.

## Commands
```bash
kubectl logs -l app=hello-app --tail=100
kubectl port-forward svc/hello-app-service 9090:80
curl http://localhost:9090/metrics
```

## Expected Result
- Logs show request flow and failures.
- `/metrics` returns text counters.

## Debugging
Use `kubectl describe pod <pod>` to correlate probe failures with logs.

## Challenge
Add one new metric for dependency latency.
