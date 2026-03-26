# 06 - Ingress and Networking

## Concept
Ingress provides HTTP routing into cluster services.

## Commands
```bash
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
kubectl get ingress
```

## Expected Result
Requests to `http://lab.local/` route to backend service.

## Debugging
- Verify ingress controller is installed.
- Minikube: `minikube addons enable ingress`
- Docker Desktop: enable Kubernetes + ingress controller setup.

## Challenge
Add a second path `/health` and route to the same service.
