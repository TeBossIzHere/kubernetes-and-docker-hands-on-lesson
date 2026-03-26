# 01 - Docker Basics

## Concept
Build and run a simple Flask container image.

## Commands
```bash
cd 01-docker-basics && \
python3 -m pip install -r requirements.txt && \
docker build -t docker-basics:v1 . && \
docker run --rm -p 5002:5002 docker-basics:v1
```

## Expected Result
- `GET /` returns hello message
- `GET /health` returns `{"status":"ok"}`

## Debugging
- View logs: `docker logs <container_id>`
- Broken dependency scenario: change `flask==3.0.3` to invalid version and rebuild
- Wrong port mapping scenario: run `-p 8080:5000` then call wrong port `:5000` to reproduce failure

## Challenge
Add an endpoint `/version` returning the image version from env var.
