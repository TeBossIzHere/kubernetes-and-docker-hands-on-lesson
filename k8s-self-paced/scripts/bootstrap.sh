#!/usr/bin/env bash
set -euo pipefail

missing=()

check_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    missing+=("$1")
  fi
}

print_install_hint() {
  local tool="$1"
  case "$tool" in
    docker)
      echo "- docker: install Docker Desktop from https://docs.docker.com/get-docker/"
      echo "  macOS (Homebrew): brew install --cask docker"
      ;;
    kubectl)
      echo "- kubectl: https://kubernetes.io/docs/tasks/tools/"
      echo "  macOS (Homebrew): brew install kubectl"
      ;;
    minikube)
      echo "- minikube (optional): https://minikube.sigs.k8s.io/docs/start/"
      echo "  macOS (Homebrew): brew install minikube"
      ;;
    python3)
      echo "- python3: install Python 3.10+"
      echo "  macOS (Homebrew): brew install python"
      ;;
  esac
}

check_cmd docker
check_cmd kubectl
check_cmd python3

if [ "${#missing[@]}" -gt 0 ]; then
  echo
  echo "Missing required dependencies:"
  for dep in "${missing[@]}"; do
    print_install_hint "$dep"
  done
  echo
  echo "After installing dependencies, run ./scripts/bootstrap.sh again."
  exit 1
fi

if [ -f requirements.txt ]; then
  echo "Installing Python dependencies from requirements.txt..."
  python3 -m pip install --upgrade pip
  python3 -m pip install -r requirements.txt
fi

if command -v minikube >/dev/null 2>&1; then
  if ! minikube status >/dev/null 2>&1; then
    echo "Starting minikube..."
    minikube start
  fi
  echo "Enabling ingress addon on minikube..."
  minikube addons enable ingress || true
else
  echo "Minikube not detected. Assuming Docker Desktop Kubernetes is enabled."
fi

echo "Bootstrap complete."
