# 05 - Config and Secrets

## Concept
Separate runtime configuration from container images.

## Commands
```bash
kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
kubectl apply -f deployment.yaml
kubectl exec deploy/configured-app -- env | grep -E 'APP_MODE|FEATURE_FLAG|API_TOKEN'
```

## Expected Result
Environment variables from ConfigMap and Secret are visible in the container.

## Debugging
Use `kubectl describe pod` and check `EnvFrom` section if variables are missing.

## Challenge
Add a new key `WELCOME_MESSAGE` and expose it through your app.
