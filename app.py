#!/usr/bin/env python3
"""NIGHTFALL Platform -- Main Application"""

import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {"status": "operational", "platform": "NIGHTFALL", "version": "0.9.2-beta"}

@app.route("/health")
def health():
    return {"healthy": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
