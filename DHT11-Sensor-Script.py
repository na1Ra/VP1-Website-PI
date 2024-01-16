import adafruit_dht
import board
import time
from datetime import datetime

def read_dht_sensor(pin):
    # DHT-Sensor initialisieren
    dht_sensor = adafruit_dht.DHT11(pin)

    # HTML-Datei öffnen
    with open('/var/www/html/output.html', 'w') as f:
        while True:
            try:
                # Temperatur und Luftfeuchtigkeit auslesen
                temperature_c = dht_sensor.temperature
                humidity = dht_sensor.humidity

                # Aktuelle Uhrzeit abrufen
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")

                # Werte und Uhrzeit in HTML-Datei schreiben
                f.write(f"<p>Uhrzeit: {current_time}, Temperatur: {temperature_c}°C, Luftfeuchtigkeit: {humidity}%</p>\n")
                f.flush()

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
