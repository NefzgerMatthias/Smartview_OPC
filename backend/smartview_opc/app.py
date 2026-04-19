import asyncio
import threading
from asyncua import Client
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# --- KONFIGURATION ---
SPS_IP = "192.168.30.2"
SPS_URL = f"opc.tcp://{SPS_IP}:4840"

NODES_CONFIG = {
    "AnalogWert": "ns=4;i=23",
    "Zylinder2Ausgefahren": "ns=4;i=3",
    "Zylinder2Eingefahren": "ns=4;i=4",
    "Zylinder3Ausgefahren": "ns=4;i=5",
    "Zylinder3Eingefahren": "ns=4;i=6",
    "StartTaster": "ns=4;i=7",
    "Zylinder1Ausfahren": "ns=4;i=8",
    "Zylinder2Ausfahren": "ns=4;i=9",
    "Zylinder2Einfahren": "ns=4;i=10",
    "Zylinder3Ausfahren": "ns=4;i=11",
    "Zylinder3Einfahren": "ns=4;i=12",
}

# Globale Variablen
sps_data = {"error": "Nicht verbunden. Bitte einloggen."}
sps_credentials = {"user": "", "pass": ""}
connection_active = False

def start_opc_fetcher():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(opc_worker())

async def opc_worker():
    global sps_data, connection_active
    while True:
        if sps_credentials["user"]:
            # Timeout auf 30 Sekunden hochsetzen
            client = Client(url=SPS_URL, timeout=30) 
            client.set_user(sps_credentials["user"])
            client.set_password(sps_credentials["pass"])
            
            try:
                async with client:
                    # Session-Überwachung etwas lockerer einstellen
                    client.secure_channel_timeout = 60000 
                    print(f"SPS-Verbindung stabilisiert für: {sps_credentials['user']}")
                    
                    connection_active = True
                    while connection_active:
                        temp_results = {}
                        try:
                            for key, node_id in NODES_CONFIG.items():
                                node = client.get_node(node_id)
                                val = await node.read_value()
                                
                                if key == "AnalogWert":
                                    temp_results[key] = round(float(val), 2)
                                else:
                                    temp_results[key] = bool(val)
                            
                            sps_data = temp_results
                            # Erhöhe die Pause auf 500ms, um die SPS zu entlasten
                            await asyncio.sleep(0.5) 
                            
                        except Exception as read_error:
                            print(f"Lese-Fehler: {read_error}")
                            # Bei einem Lesefehler nicht sofort abbrechen, sondern kurz warten
                            await asyncio.sleep(1)
                            break # Innere Schleife verlassen -> Reconnect

            except Exception as e:
                print(f"SPS Verbindungsfehler: {e}")
                sps_data = {"error": "Verbindung unterbrochen. Reconnect läuft..."}
                connection_active = False
                
        # Längere Pause vor dem nächsten Verbindungsversuch (wichtig!)
        await asyncio.sleep(5)

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/login")
def api_login():
    global sps_credentials, connection_active
    data = request.json
    sps_credentials["user"] = data.get("username")
    sps_credentials["pass"] = data.get("password")
    connection_active = False # Bestehende Verbindung kappen, um neu zu starten
    return jsonify({"status": "Login-Daten empfangen, verbinde zur SPS..."})

@app.get("/api/tags")
def api_tags():
    return jsonify(sps_data)

if __name__ == "__main__":
    thread = threading.Thread(target=start_opc_fetcher, daemon=True)
    thread.start()
    app.run(host="0.0.0.0", port=5000, debug=False)