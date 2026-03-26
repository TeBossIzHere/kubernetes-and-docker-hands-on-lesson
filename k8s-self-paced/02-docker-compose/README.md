# 02 - Docker Compose

## Concept
Run multi-service apps with built-in DNS networking and dependency management.

## Commands
```bash
cd 02-docker-compose
python3 -m pip install -r requirements.txt
docker compose up --build
```

## Expected Result
Requests to `http://localhost:5000/` increase Redis-backed hit counter.

## Debugging
- Check service networking: `docker compose exec web ping redis`
- Redis failure scenario: stop redis container and hit endpoint to observe retry logic
- View logs: `docker compose logs -f`

## Challenge
Add a second Flask endpoint that reads a custom key from Redis.
