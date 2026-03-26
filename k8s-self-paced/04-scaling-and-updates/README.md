# 04 - Scaling and Updates

## Concept
Scale deployments and perform zero-downtime rolling updates.

## Commands
```bash
kubectl apply -f deployment.yaml
kubectl scale deployment hello-app-rollout --replicas=4
kubectl set image deployment/hello-app-rollout hello-app=docker-k8s-lab:v2
kubectl rollout status deployment/hello-app-rollout
```

## Expected Result
Replicas scale to 4 and image updates from v1 to v2 gradually.

## Debugging
Use `kubectl rollout history deployment hello-app-rollout` and `kubectl describe` to inspect update behavior.

## Challenge
Perform rollback: `kubectl rollout undo deployment/hello-app-rollout`.
