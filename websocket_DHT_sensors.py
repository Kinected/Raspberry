import asyncio
import json
import websockets
import Adafruit_DHT

# Spécifiez le type de capteur (DHT11 ou DHT22) et le numéro de broche GPIO
capteur = Adafruit_DHT.DHT11
broche = 18

async def send_temperature():
    uri = "ws://172.20.10.3:8000/ws/sensors"  # Remplacez par l'URL WebSocket appropriée
    while True:
        try:
            async with websockets.connect(uri) as websocket:
                while True:
                    humidite, temperature = Adafruit_DHT.read_retry(capteur, broche)
                    if humidite is not None and temperature is not None:
                        sensors_data = {
                            'temperature': temperature,
                            'humidity': humidite
                        }
                        sensors_json = json.dumps(sensors_data)
                        await websocket.send(sensors_json)
                    else:
                        print('Échec de la lecture du capteur. Réessayer!')
                    await asyncio.sleep(2)  # Attendre 2 secondes avant d'envoyer la prochaine température
                    print('Température={0:0.1f}*C  Humidité={1:0.1f}%'.format(temperature, humidite))
        except websockets.exceptions.ConnectionClosedError:
            print("La connexion WebSocket a été fermée. Tentative de reconnexion...")
            await asyncio.sleep(5)  # Attendre 5 secondes avant de tenter une reconnexion


asyncio.run(send_temperature())