IMAGE_NAME ?= docker-k8s-lab
IMAGE_TAG ?= v1
K8S_DIR ?= 03-kubernetes-basics

.PHONY: doctor build run deploy ingress clean logs

doctor:
	@command -v python3 >/dev/null 2>&1 || (echo "Missing python3. Install: brew install python"; exit 1)
	@command -v docker >/dev/null 2>&1 || (echo "Missing docker. Install Docker Desktop: https://docs.docker.com/get-docker/"; exit 1)
	@command -v kubectl >/dev/null 2>&1 || (echo "Missing kubectl. Install: https://kubernetes.io/docs/tasks/tools/"; exit 1)
	@echo "Environment check passed."

build:
	@command -v docker >/dev/null 2>&1 || (echo "Missing docker. Install Docker Desktop first."; exit 1)
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) 01-docker-basics

run:
	@command -v docker >/dev/null 2>&1 || (echo "Missing docker. Install Docker Desktop first."; exit 1)
	docker run --rm -p 5000:5000 --name docker-k8s-lab $(IMAGE_NAME):$(IMAGE_TAG)

deploy:
	kubectl apply -f $(K8S_DIR)/deployment.yaml
	kubectl apply -f $(K8S_DIR)/service.yaml

ingress:
	kubectl apply -f 06-ingress-and-networking/ingress.yaml

clean:
	./scripts/reset.sh

logs:
	kubectl logs -l app=hello-app --tail=100
