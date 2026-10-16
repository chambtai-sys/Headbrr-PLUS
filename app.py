#!/usr/bin/env python3
"""Headbrr PLUS - local web server. Usage: python app.py [--port 5000] [--host 127.0.0.1]"""
import argparse
from flask import Flask, render_template

app = Flask(__name__)
VERSION = "2.0.0"


@app.route("/")
def index():
    return render_template("index.html", version=VERSION)


@app.route("/health")
def health():
    return {"ok": True, "name": "Headbrr PLUS", "version": VERSION}


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Headbrr PLUS headphone tester")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=5000)
    a = p.parse_args()
    print(f"Headbrr PLUS v{VERSION} -> http://{a.host}:{a.port}")
    app.run(host=a.host, port=a.port, debug=False)
