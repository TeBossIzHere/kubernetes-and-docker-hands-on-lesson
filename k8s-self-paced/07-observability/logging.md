# Logging Guide

## Using kubectl logs

```bash
kubectl logs -l app=hello-app --tail=100
kubectl logs <pod-name> -c hello-app -f
```

## Best Practices

- Log in structured or consistent plain text format.
- Write logs to stdout/stderr only.
- Include request context and error details.
- Avoid logging secrets and tokens.
