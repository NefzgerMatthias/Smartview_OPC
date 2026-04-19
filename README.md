# 🚀 SmartView OPC – Prozessdaten-Visualisierung (Read-Only)

Dieses Projekt ist ein kompaktes **SCADA-System** (Supervisory Control and Data Acquisition). Es dient als Edge-Gateway, um Prozessdaten einer Siemens S7-1200 via OPC UA zu erfassen und auf einem modernen Web-Dashboard darzustellen.

**Hinweis:** Das System ist als reines Monitoring-Tool konzipiert. Es findet kein Schreibzugriff auf die SPS statt (Read-Only).

## 📋 Projektbeschreibung
Das System überwacht ein pneumatisches Versuchsboard in Echtzeit. Als zentrale Schnittstelle dient ein Raspberry Pi 4B, der die Lücke zwischen der Feldebene (SPS) und der IT-Ebene (Browser) schließt.

### Überwachte Komponenten:
* **Zylinder-Status:** Überwachung von einem einfachwirkenden und zwei doppeltwirkenden Pneumatikzylindern (Endlagenabfrage).
* **Analogwert:** Visualisierung eines manuell einstellbaren Potenziometers (Widerstandswert/Spannung).
* **Aktoren-Feedback:** Anzeige des aktuellen Schaltzustands der Zylinder-Ansteuerung.

## 🏗️ Systemarchitektur (ISA-95 Modell)
1. **Feldebene:** Siemens SIMATIC S7-1200 (OPC UA Server).
2. **Edge-Ebene:** Raspberry Pi 4B (Python OPC UA Client & Flask REST-API).
3. **Leitebene:** Web-Browser (Responsive Frontend mit Polling-Verfahren alle 500ms).

## 🛠️ Einrichtung & Setup

### 1. Hardware & Netzwerk
* **Verbindung:** S7-1200 und Raspberry Pi sind über ein **LAN-Kabel** direkt verbunden.
* **Raspberry Pi IP (Hotspot):** `192.168.137.208`
* **SPS IP:** `192.168.30.2` (Sicherstellen, dass der Pi im selben Subnetz konfiguriert ist).

### 2. Software-Installation
Installieren Sie die benötigten Python-Bibliotheken:
```bash
pip install flask flask-cors asyncua