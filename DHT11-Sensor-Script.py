import adafruit_dht
import board
import time

def read_dht_sensor(pin):
    # DHT-Sensor initialisieren
    dht_sensor = adafruit_dht.DHT11(pin)

    try:
        while True:
            try:
                # Temperatur und Luftfeuchtigkeit auslesen
                temperature_c = dht_sensor.temperature
                humidity = dht_sensor.humidity

                # Rückgabe der Werte
                return temperature_c, humidity

            except RuntimeError as e:
                # Fehlermeldung ausgeben
                print(f"Fehler beim Auslesen des Sensors: {e}")

                # Sensor neu starten
                dht_sensor.exit()
                dht_sensor = adafruit_dht.DHT11(pin)

            # Wartezeit erhöhen
            time.sleep(5)

    except KeyboardInterrupt:
        # Programm beenden, wenn eine Tastenunterbrechung erfolgt
        pass

    finally:
        # Sensor freigeben
        dht_sensor.exit()

# Beispielaufruf der Funktion
temperature, humidity = read_dht_sensor(board.D4)
print(f"Temperatur: {temperature}°C, Luftfeuchtigkeit: {humidity}%")
