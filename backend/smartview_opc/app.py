from __future__ import annotations
import time
from typing import Any, Dict
from flask import Flask, jsonify, render_template, Response

# Flask Instanz mit Pfaden zu deinen Ordnern
app = Flask(__name__, static_folder="static", template_folder="templates")

@app.get("/")
def home():
    return render_template("index.html")

def get_current_tags() -> Dict[str, Any]:
    now = time.time()
    # Simulation deiner Hardware
    return {
        "zylinder_feder": {
            "name": "Zylinder 1 (Feder-Rückzug)",
            "eingefahren": (int(now) % 6) < 3,
            "ausgefahren": (int(now) % 6) >= 4,
            "typ": "monostabil"
        },
        "zylinder_elektro_1": {
            "name": "Zylinder 2 (Elektro-Pneu A)",
            "eingefahren": (int(now) % 8) < 4,
            "ausgefahren": (int(now) % 8) >= 5,
            "typ": "bistabil"
        },
        "zylinder_elektro_2": {
            "name": "Zylinder 3 (Elektro-Pneu B)",
            "eingefahren": (int(now) % 10) < 5,
            "ausgefahren": (int(now) % 10) >= 6,
            "typ": "bistabil"
        },
        "analog_sensor": {
            "name": "Drucksensor / Spannung",
            "value": round((now % 24), 2), # Simuliert 0V bis 24V
            "unit": "V",
            "min": 0,
            "max": 24
        }
    }

@app.after_request
def add_cors_headers(resp: Response) -> Response:
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

@app.get("/api/tags")
def api_tags():
    return jsonify(get_current_tags())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)