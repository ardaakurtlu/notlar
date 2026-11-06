import logging
from flask import Flask, request

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("portfolio")

@app.before_request
def log_request():
    log.info("%s %s", request.method, request.path)

@app.get("/")
def home():
    return "Ubuntu server project is running.\n"

@app.get("/health")
def health():
    return {"status": "ok"}
