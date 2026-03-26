import os
import time
import logging
from flask import Flask, jsonify
import redis

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

REDIS_HOST = os.getenv("REDIS_HOST", "redis")


def get_redis_client(max_retries=5, delay=2):
    for attempt in range(1, max_retries + 1):
        try:
            client = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)
            client.ping()
            return client
        except redis.RedisError as err:
            app.logger.warning("Redis unavailable (attempt %s/%s): %s", attempt, max_retries, err)
            time.sleep(delay)
    raise RuntimeError("Unable to connect to Redis after retries")


@app.route("/")
def root():
    client = get_redis_client()
    count = client.incr("hits")
    return jsonify(message="Hello from Flask + Redis", hits=count)


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
