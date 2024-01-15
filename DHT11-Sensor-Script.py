import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio=False)

def get_temp_humidity():
    while True:
        try:
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            return temperature_c, humidity
        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error

# Außerhalb der Funktion
temp, hum = get_temp_humidity()
print("Temp: {:.1f} C Humidity: {}% ".format(temp, hum))
