# 00 - Introduction

## Concept

- Containers package app + runtime dependencies.
- VMs virtualize an entire OS; containers share host kernel.
- Kubernetes orchestrates container scheduling, networking, scaling, and self-healing.

## Course Architecture

This course starts with single-container Docker workflows, then expands to Docker Compose, then to Kubernetes primitives and production patterns.

## Install Tooling (one-time)

- Docker Desktop: https://docs.docker.com/get-docker/
- kubectl: https://kubernetes.io/docs/tasks/tools/
- Minikube (optional): https://minikube.sigs.k8s.io/docs/start/

## Setup Commands

```bash
cd k8s-self-paced
# Python dependencies for lesson apps
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r ./requirements.txt

# Verify container and cluster tooling
docker --version
kubectl version --client
minikube version # optional
make doctor
```

Enable Kubernetes in Docker Desktop or run:

```bash
minikube start
minikube addons enable ingress
```

## Expected Result

You can run Docker containers and execute `kubectl get nodes` successfully.

## Debugging

- If `kubectl` cannot connect, verify kube context: `kubectl config get-contexts`
- If ingress unavailable on Minikube, re-enable addon and wait for controller pods.

## Challenge

Switch kube contexts between Docker Desktop and Minikube and verify node status each time.
