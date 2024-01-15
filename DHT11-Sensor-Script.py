import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio=False)

def get_temp_humidity():
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        return temperature_c, humidity
    except RuntimeError as error:
        print(error.args[0])
        return None, None
    except Exception as error:
        dhtDevice.exit()
        raise error

# Außerhalb der Funktion
while True:
    temp, hum = get_temp_humidity()
    if temp is not None and hum is not None:
        print("Temp: {:.1f} C Humidity: {}% ".format(temp, hum))
    time.sleep(2.0)  # Wartezeit von 2 Sekunden zwischen den Messungen
