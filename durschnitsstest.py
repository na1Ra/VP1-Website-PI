import adafruit_dht
import board
import time

def read_dht_sensor(pin):
    # DHT-Sensor initialisieren
    dht_sensor = adafruit_dht.DHT11(pin)

    # Dateipfad für die Speicherung der Daten
    data_file_path = '/home/admin/GIT/VP1-Website-PI/data.txt'

    # Liste fÃ¼r die Speicherung der letzten 2 EintrÃ¤ge
    data = []

    # Liste fÃ¼r den Durchschnitt der Temperatur und Luftfeuchtigkeit
    average_data = []

    while True:
        try:
            # Temperatur und Luftfeuchtigkeit auslesen
            temperature_c = dht_sensor.temperature
            humidity = dht_sensor.humidity

            # Werte zur Liste hinzufügen und Formatieren
            data.append(f'Temperature={temperature_c};Humidity={humidity}')

            # Wenn mehr als 2 EintrÃ¤ge in der Liste sind, den Ã¤ltesten Eintrag entfernen
            if len(data) > 2:
                data.pop(0)

            # Durchschnitt berechnen und zur Liste hinzufügen
            if len(data) == 2:
                avg_temperature = sum(entry.temperature for entry in data) / 2
                avg_humidity = sum(entry.humidity for entry in data) / 2
                average_data.append(f'Average_Temperature={avg_temperature};Average_Humidity={avg_humidity}')

            # Wenn mehr als 2 Einträge im Durchschnitts-Daten sind, den Ältesten Eintrag entfernen
            if len(average_data) > 2:
                average_data.pop(0)

            # HTML-Datei Öffnen, den Hintergrund erstellen und die Daten schreiben
            with open('/home/admin/GIT/VP1-Website-PI/output.html', 'w') as f:
                f.write('<html><body style="background-color:black;">')
                for entry in data + average_data:
                    f.write(f'<div>{entry}</div>')
                f.write('</body></html>')

            # Daten in Textdatei speichern
            with open(data_file_path, 'w') as data_file:
                for entry in data + average_data:
                    data_file.write(f'{entry}\n')

        except RuntimeError as e:
            # Fehlermeldung ausgeben
            print(f"Fehler beim Auslesen des Sensors: {e}")

            # Sensor neu starten
            dht_sensor.exit()
            dht_sensor = adafruit_dht.DHT11(pin)

            # Daten aus der Textdatei wieder einlesen
            try:
                with open(data_file_path, 'r') as data_file:
                    lines = data_file.readlines()
                    data = [line.strip() for line in lines]
            except FileNotFoundError:
                # Wenn die Datei nicht gefunden wird, einfach fortfahren
                pass

        # Wartezeit erhöhen
        time.sleep(5)

# Aufruf der Funktion
read_dht_sensor(board.D4)
