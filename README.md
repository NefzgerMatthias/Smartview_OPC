# SmartView OPC

**Prozessdaten im Griff – Ein einfaches SCADA-System auf Basis von OPC UA**


## Projektbeschreibung & Ziel

Ihr seid Teil der modernen Industrie 4.0 – einer Welt, in der Maschinen miteinander sprechen, Daten in Echtzeit fließen und Entscheidungen auf Basis präziser Informationen getroffen werden. Damit das funktioniert, braucht es Systeme, die Prozesse überwachen, Daten sammeln und verständlich darstellen: sogenannte SCADA-Systeme (Supervisory Control and Data Acquisition).

In diesem Projekt entwickelt ihr euer eigenes kleines SCADA-System:
**„SmartView OPC – Prozessdaten im Griff“**

Euer System liest über den Standard OPC UA Daten von einer Siemens S7-1200 aus und zeigt sie auf einer modernen, responsiven Webseite an. Als Hardware dient ein Raspberry Pi 4B, der als Edge Device arbeitet – eine Schlüsseltechnologie für die vernetzte Produktion der Zukunft.

### Warum ist das wichtig?

* Industrie 4.0 lebt von Transparenz und Vernetzung
* Echtzeit-Daten ermöglichen höhere Effizienz und Qualität
* Edge Devices wie der Raspberry Pi bringen Intelligenz direkt an die Maschine
* OPC UA sorgt für sichere, herstellerunabhängige Kommunikation zwischen Steuerungen und IT-Systemen


## Kurzanleitung (Start in 2–3 Befehlen)

Verbindung zum Raspberry Pi (z. B. über VS Code Remote SSH):

```bash
pi@192.168.30.50
```
Passwort eingeben
```bash
pi
```

Anwendung starten:

```bash
cd Smartview_OPC
python backend/smartview_opc/app.py
```

Erreichbar unter:

```text
http://192.168.30.50:5000
```


## Nutzung über VS Code (Remote)

1. VS Code öffnen
2. Erweiterung **Remote - SSH** verwenden
3. Verbindung herstellen:

   ```
   pi@192.168.30.50
   ```
4. Projektordner `Smartview_OPC` öffnen
5. Terminal in VS Code nutzen und Anwendung starten


## Konfiguration (OPC Endpoint & NodeIds)

Die Konfiguration erfolgt aktuell direkt im Code:

Datei:

```text
backend/smartview_opc/app.py
```

### OPC Endpoint

```python
SPS_IP = "192.168.30.2"
SPS_URL = f"opc.tcp://{SPS_IP}:4840"
```


### NodeIds

```python
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
```


## Architekturdiagramm

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/dfe3376c-6412-4258-afba-73e1e3eb0ef0" />


## Systemübersicht

* Backend: Flask (Python)
* Kommunikation: OPC UA (`asyncua`)
* Hardware: Raspberry Pi 4B
* Frontend: HTML / CSS / JavaScript
* Datenaktualisierung: Polling (~500 ms)


## Bekannte Einschränkungen

* Konfiguration aktuell im Code
* Globale Zustände im Backend
* Polling statt OPC UA Subscriptions
* Kein Benutzer-/Session-Management


## Team

Matthias Nefzger 
Leon Schwartz


