# 03 - Kubernetes Basics

## Concept
Deploy a containerized app via Deployment and expose internally via ClusterIP Service.

## Commands
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get pods
kubectl get svc
```

## Expected Result
Two healthy pods become Ready and service routes traffic to them.

## Debugging
- Inspect logs: `kubectl logs -l app=hello-app`
- Inspect resources: `kubectl describe deployment hello-app`
- Check probe events if pods restart.

## Challenge
Change replicas from 2 to 3 and verify load-balancing behavior.
