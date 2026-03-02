from backend.smartview_opc.app import app

if __name__ == "__main__":
    # Dies startet deinen Flask-Server
    print("Starte SmartView OPC Server auf http://localhost:5000...")
    app.run(host="0.0.0.0", port=5000, debug=True)