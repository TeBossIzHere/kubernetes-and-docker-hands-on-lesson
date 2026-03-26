import os
from flask import Flask, jsonify
import redis

app = Flask(__name__)
REQUESTS_TOTAL = 0

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
APP_ENV = os.getenv("APP_ENV", "dev")


def redis_client():
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


@app.route('/api/health')
def health():
    return jsonify(status='ok', env=APP_ENV)


@app.route('/api/count')
def count():
    global REQUESTS_TOTAL
    REQUESTS_TOTAL += 1
    r = redis_client()
    hits = r.incr('api_hits')
    return jsonify(hits=hits, requests_total=REQUESTS_TOTAL)


@app.route('/metrics')
def metrics():
    r = redis_client()
    redis_up = 1
    try:
        r.ping()
    except redis.RedisError:
        redis_up = 0
    return (
        f"app_requests_total {REQUESTS_TOTAL}\n"
        f"app_up 1\n"
        f"redis_up {redis_up}\n",
        200,
        {'Content-Type': 'text/plain; version=0.0.4'}
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
