# backend/smartview_opc/app.py
from __future__ import annotations

import time
from typing import Any, Dict

from flask import Flask, jsonify, abort,render_template

from flask import Response, request



app = Flask(__name__, static_folder="static", template_folder="templates")

@app.get("/")
def home():
    return render_template("index.html")

# Dummy-Tags (mind. 3, davon mind. 1 analog)
# Später ersetzt ihr die Werte durch echte OPC-UA Reads.
def get_current_tags() -> Dict[str, Dict[str, Any]]:
    now = time.time()
    return {
        "temperature": {"value": round(20.0 + (now % 10) * 0.1, 2), "unit": "°C", "type": "analog"},
        "pressure": {"value": round(1.0 + (now % 5) * 0.05, 3), "unit": "bar", "type": "analog"},
        "motor_running": {"value": int(now) % 2 == 0, "unit": "", "type": "digital"},
    }

# Mini-CORS: damit ihr frontend/index.html lokal öffnen könnt und trotzdem fetch klappt
@app.after_request
def add_cors_headers(resp: Response) -> Response:
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
    resp.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    return resp


@app.get("/api/tags")
def api_tags():
    return jsonify(get_current_tags())


@app.get("/api/tags/<name>")
def api_tag_single(name: str):
    tags = get_current_tags()
    if name not in tags:
        abort(404, description=f"Unknown tag: {name}")
    return jsonify({name: tags[name]})


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    # host=0.0.0.0 ist praktisch, wenn ihr vom Handy/anderen PC im LAN testen wollt.
    app.run(host="0.0.0.0", port=5000, debug=True)
    