import adafruit_dht
import board
import time
from datetime import datetime

def read_dht_sensor(pin):
    # DHT-Sensor initialisieren
    dht_sensor = adafruit_dht.DHT11(pin)

    # Liste für die Speicherung der letzten 8 Einträge
    data = []

    while True:
        try:
            # Temperatur und Luftfeuchtigkeit auslesen
            temperature_c = dht_sensor.temperature
            humidity = dht_sensor.humidity

            # Aktuelle Uhrzeit abrufen
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            # Werte und Uhrzeit zur Liste hinzufügen
            data.append(f'<div style="background-color:gray; width:100px; height:40px; position:relative;"><div style="background-color:red; width:{temperature_c}px; height:40px;"></div><span style="position:absolute; left:5px; color:white;">{temperature_c}°C</span></div>;<div style="background-color:gray; width:100px; height:40px; position:relative;"><div style="background-color:blue; width:{humidity}px; height:40px;"></div><span style="position:absolute; left:5px; color:white;">{humidity}%</span></div>')

            # Wenn mehr als 8 Einträge in der Liste sind, den ältesten Eintrag entfernen
            if len(data) > 1:
                data.pop(0)

            # HTML-Datei öffnen und die Daten schreiben
            with open('/var/www/html/output.html', 'w') as f:
                f.write('<html><body style="background-color:black;">')
                for entry in data:
                    f.write(entry)
                f.write('</body></html>')

        except RuntimeError as e:
            # Fehlermeldung ausgeben
            print(f"Fehler beim Auslesen des Sensors: {e}")

            # Sensor neu starten
            dht_sensor.exit()
            dht_sensor = adafruit_dht.DHT11(pin)

        # Wartezeit erhöhen
        time.sleep(5)

# Beispielaufruf der Funktion
read_dht_sensor(board.D4)
