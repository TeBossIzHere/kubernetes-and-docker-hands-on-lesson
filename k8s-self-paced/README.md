# Kubernetes & Docker Self-Paced Learning Lab

A production-aware, beginner-friendly lab to learn Docker and Kubernetes with incremental modules.

## Prerequisites

- Docker Desktop with Kubernetes enabled **or** Minikube
- kubectl
- make
- Python 3.10+

Install links:
- Docker Desktop: https://docs.docker.com/get-docker/
- kubectl: https://kubernetes.io/docs/tasks/tools/
- Minikube (optional): https://minikube.sigs.k8s.io/docs/start/

## Quick Start

```bash
cp .env.example .env
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
make doctor
./scripts/bootstrap.sh
make build
make run
```

Then work through modules in sequence:

1. `00-intro`
2. `01-docker-basics`
3. `02-docker-compose`
4. `03-kubernetes-basics`
5. `04-scaling-and-updates`
6. `05-config-and-secrets`
7. `06-ingress-and-networking`
8. `07-observability`
9. `08-fullstack-project`
10. `09-failure-scenarios`
11. `challenges`

## Local Runtime Targets

- Docker-only modules run locally with Docker Engine.
- Kubernetes modules work with Minikube or Docker Desktop Kubernetes.

## Real-World Patterns Covered

- Container health checks
- Liveness/readiness probes
- ConfigMap and Secret usage
- Rolling updates and versioned images
- Ingress routing
- Basic observability (`/metrics`, logs)
- Intentional failure debugging

## CI/CD

- `.github/workflows/docker-build.yml` validates Docker image build and Dockerfile
- `.github/workflows/k8s-validate.yml` performs Kubernetes manifest dry-run validation

## Reset Environment

```bash
./scripts/reset.sh
```
