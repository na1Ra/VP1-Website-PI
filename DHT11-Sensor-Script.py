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
            data.append(f"<p>Uhrzeit: {current_time}, Temperatur: {temperature_c}°C, Luftfeuchtigkeit: {humidity}%</p>\n")

            # Wenn mehr als 8 Einträge in der Liste sind, den ältesten Eintrag entfernen
            if len(data) > 8:
                data.pop(0)

            # HTML-Datei öffnen und die Daten schreiben
            with open('/var/www/html/output.html', 'w') as f:
                for entry in data:
                    f.write(entry)

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
