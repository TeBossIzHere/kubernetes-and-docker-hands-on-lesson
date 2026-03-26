import logging
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


@app.route("/")
def root():
    app.logger.info("Root endpoint called")
    return jsonify(message="Hello World from Docker Basics")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.errorhandler(Exception)
def handle_error(error):
    app.logger.error("Unhandled error: %s", error)
    return jsonify(error="internal server error"), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
