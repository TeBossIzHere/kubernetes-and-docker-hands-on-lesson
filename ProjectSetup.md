# PROJECT SPEC V2: Kubernetes & Docker Self-Paced Learning Lab (Production-Grade)

## Overview

Build a fully self-contained, locally runnable GitHub repository that teaches Docker and Kubernetes through progressive, hands-on modules with production-oriented practices.

This version MUST include:
- CI/CD pipelines
- Observability (logs + basic metrics exposure)
- Ingress-based routing
- Failure injection scenarios
- Interview-style debugging exercises

The repository must function as:
1. A self-paced course
2. A hands-on lab environment
3. A portfolio-quality project

---

## High-Level Structure

k8s-self-paced/
├── README.md
├── Makefile
├── .env.example
├── scripts/
│   ├── reset.sh
│   └── bootstrap.sh
├── .github/
│   └── workflows/
│       ├── docker-build.yml
│       └── k8s-validate.yml
├── 00-intro/
│   └── README.md
├── 01-docker-basics/
│   ├── README.md
│   ├── app/
│   │   └── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── 02-docker-compose/
│   ├── README.md
│   ├── docker-compose.yml
│   └── app/
│       └── app.py
├── 03-kubernetes-basics/
│   ├── README.md
│   ├── deployment.yaml
│   └── service.yaml
├── 04-scaling-and-updates/
│   ├── README.md
│   └── deployment.yaml
├── 05-config-and-secrets/
│   ├── README.md
│   ├── configmap.yaml
│   ├── secret.yaml
│   └── deployment.yaml
├── 06-ingress-and-networking/
│   ├── README.md
│   ├── ingress.yaml
│   └── service.yaml
├── 07-observability/
│   ├── README.md
│   ├── logging.md
│   └── metrics.md
├── 08-fullstack-project/
│   ├── README.md
│   ├── frontend/
│   ├── backend/
│   ├── docker-compose.yml
│   └── k8s/
│       ├── deployment.yaml
│       ├── service.yaml
│       └── ingress.yaml
├── 09-failure-scenarios/
│   ├── README.md
│   └── broken-deployment.yaml
└── challenges/
    ├── README.md
    └── interview.md

---

## Global Requirements

- All services must run locally
- Support:
  - Docker Desktop (with Kubernetes enabled) OR Minikube
- Backend must use Python (Flask or FastAPI)
- Use minimal but production-relevant configurations
- No hardcoded IPs (use service discovery)
- All YAML must be valid and well-commented
- Include health checks (liveness/readiness where applicable)

---

## Module Specifications

### 00 - Introduction

Explain:
- Containers vs VMs
- Kubernetes core concepts
- Architecture of the course

Include:
- Setup instructions:
  - Docker Desktop OR Minikube
  - kubectl
  - Enable Kubernetes

### 01 - Docker Basics

Deliver:
- Flask app with:
  - `/` → Hello World
  - `/health`
- Dockerfile (`python:3.10-slim`)

Enhancements:
- Add logging to stdout
- Add basic error handling

README must include:
- Build/run commands
- Inspect container logs
- Debug scenarios:
  - Broken dependency
  - Wrong port mapping

### 02 - Docker Compose

Deliver:
- Flask + Redis system

Enhancements:
- Add retry logic when Redis is unavailable

README:
- Service networking explanation
- Debug:
  - Redis connection failure

### 03 - Kubernetes Basics

Deliver:
- Deployment (2 replicas)
- Service (ClusterIP)

Enhancements:
- Add livenessProbe
- Add readinessProbe

README:
- `kubectl logs`
- `kubectl describe`

### 04 - Scaling and Updates

Enhancements:
- Rolling update strategy
- Image versioning concept

Exercise:
- Deploy v1 → update to v2

### 05 - Config and Secrets

Enhancements:
- Inject env variables via ConfigMap
- Inject sensitive data via Secret

### 06 - Ingress and Networking

Goal: Expose services externally

Deliver:
- `ingress.yaml`

Requirements:
- Route `/` to backend service

README:
- Explain Ingress controller
- Setup instructions (Minikube ingress addon or Docker Desktop)

### 07 - Observability

Goal: Teach visibility into systems

Deliver:
- `logging.md`
  - Using `kubectl logs`
  - Container logging best practices
- `metrics.md`
  - Expose simple `/metrics` endpoint (text-based)
  - Explain Prometheus conceptually

Backend must:
- Include a `/metrics` endpoint

### 08 - Fullstack Project

Build:
- Frontend (simple UI)
- Backend API
- Redis

Enhancements:
- Add environment configs
- Add health checks
- Add ingress routing

Architecture:

User → Ingress → Frontend → Backend → Redis

### 09 - Failure Scenarios

Goal: Teach debugging

Deliver broken configs:
- Invalid image tag
- CrashLoopBackOff scenario
- Misconfigured service selector

README:
- Ask user to diagnose and fix

---

## Challenges

### challenges/README.md

Hands-on tasks:
- Scale system to 5 replicas
- Add new environment variable
- Add new service

### challenges/interview.md

Include questions like:
- Why is my pod restarting?
- Difference between Deployment and Pod
- How does service discovery work?

---

## Root-Level Tooling

### Makefile

Include:
- `make build`
- `make run`
- `make deploy`
- `make ingress`
- `make clean`
- `make logs`

### reset.sh

Must:
- Stop and remove containers
- Clean Docker images safely
- Delete Kubernetes resources

### bootstrap.sh

Must:
- Verify dependencies
- Start Minikube (if used)
- Enable ingress

---

## CI/CD (GitHub Actions)

### docker-build.yml

- Build Docker image
- Validate Dockerfile

### k8s-validate.yml

- Lint Kubernetes YAML
- Basic validation (`kubectl apply --dry-run=client`)

---

## README Quality Requirements

Each module must include:
1. Concept
2. Commands
3. Expected result
4. Debugging section
5. Challenge

---

## Observability Requirements

- All services log to stdout
- Backend exposes `/metrics`
- README explains:
  - logs
  - metrics basics

---

## Failure Philosophy

Each major section must include:
- At least one intentional failure scenario
- Instructions to debug using:
  - logs
  - `kubectl describe`
  - `kubectl get`

---

## Final Output Expectations

The generated repository must:
- Run locally without modification
- Be beginner-friendly but production-aware
- Demonstrate real-world patterns:
  - health checks
  - config separation
  - scaling
  - ingress routing
- Be portfolio-ready

Avoid:
- Overly complex frameworks
- Missing instructions
- Non-functional configs

Prioritize:
- Clarity
- Hands-on learning
- Real engineering workflows

END OF SPEC V2