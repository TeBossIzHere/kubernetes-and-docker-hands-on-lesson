# 08 - Fullstack Project

## Concept
Build and deploy a simple fullstack architecture:

User → Ingress → Frontend → Backend → Redis

## Commands
```bash
cd 08-fullstack-project
python3 -m pip install -r ../requirements.txt
docker compose up --build
# Kubernetes
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
```

## Expected Result
- Frontend UI loads in browser.
- UI button calls backend API and increments Redis counter.
- `/metrics` endpoint is available on backend service.

## Debugging
- `kubectl logs deploy/backend`
- `kubectl describe ingress fullstack-ingress`
- Verify service endpoints: `kubectl get endpoints`

## Challenge
Add another backend endpoint returning deployment metadata via env vars.
