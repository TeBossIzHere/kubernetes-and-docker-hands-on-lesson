#!/usr/bin/env bash
set -euo pipefail

echo "Stopping known containers..."
docker rm -f docker-k8s-lab compose-web compose-redis fullstack-frontend fullstack-backend fullstack-redis 2>/dev/null || true

echo "Pruning dangling images..."
docker image prune -f

echo "Deleting Kubernetes resources from module directories..."
for d in 03-kubernetes-basics 04-scaling-and-updates 05-config-and-secrets 06-ingress-and-networking 08-fullstack-project/k8s 09-failure-scenarios; do
  if [ -d "$d" ]; then
    kubectl delete -f "$d" --ignore-not-found=true 2>/dev/null || true
  fi
done

echo "Reset complete."
