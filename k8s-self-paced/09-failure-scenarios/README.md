# 09 - Failure Scenarios

## Concept
Practice diagnosing and fixing realistic Kubernetes failures.

## Commands
```bash
kubectl apply -f broken-deployment.yaml
kubectl get pods
kubectl describe pod -l app=broken-app
kubectl get svc broken-service
kubectl get endpoints broken-service
```

## Expected Result
You should observe:
- Image pull failure (`ErrImagePull`/`ImagePullBackOff`)
- CrashLoopBackOff behavior
- Service with no endpoints due to selector mismatch

## Debugging Tasks
1. Fix image tag.
2. Replace crash command with a real startup command.
3. Correct service selector label.

## Challenge
Add liveness/readiness probes and intentionally misconfigure one probe, then debug.
