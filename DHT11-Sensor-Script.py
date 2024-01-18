import adafruit_dht
import board
import time

def read_dht_sensor(pin):
    #DHT-Sensor initialisieren
    dht_sensor = adafruit_dht.DHT11(pin)

    #Liste für die Speicherung der letzten 2 Einträge
    data = []

    while True:
        try:
            #Temperatur und Luftfeuchtigkeit auslesen
            temperature_c = dht_sensor.temperature
            humidity = dht_sensor.humidity

            #Werte zur Liste hinzufügen und Formatieren
            data.append(f'<div style="background-color:gray; width:100%; height:20%; position:relative;"><div style="background-color:red; width:{temperature_c}%; height:100%;"></div><span style="position:absolute; left:5px; color:white; font-family: Arial ;">{temperature_c}°C</span></div>;
            <div style="background-color:gray; width:100%; height:20%; position:relative;"><div style="background-color:blue; width:{humidity}%; height:100%;"></div><span style="position:absolute; left:5px; color:white; font-family: Arial ;">{humidity}%</span></div>')

            #Wenn mehr als 2 Einträge in der Liste sind, den ältesten Eintrag entfernen
            if len(data) > 1:
                data.pop(0)

            #HTML-Datei öffnen den Hintergrung erstellen und die Daten schreiben
            with open('/var/www/html/output.html', 'w') as f:
                f.write('<html><body style="background-color:black;">')
                for entry in data:
                    f.write(entry)
                f.write('</body></html>')

        except RuntimeError as e:
            #Fehlermeldung ausgeben
            print(f"Fehler beim Auslesen des Sensors: {e}")

            #Sensor neu starten
            dht_sensor.exit()
            dht_sensor = adafruit_dht.DHT11(pin)

        #Wartezeit erhöhen
        time.sleep(5)

#Aufruf der Funktion
read_dht_sensor(board.D4)
