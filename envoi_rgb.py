import websocket
import json

# URL du serveur websocket sur la Raspberry Pi
server_url = "ws://172.20.10.4:8000/ws/leds"

# Données à envoyer
data = {"type": "RGB", "value": (255, 0, 0)}

# Convertir les données en JSON
data_json = json.dumps(data)

# Fonction appelée lorsque la connexion est établie
def on_open(ws):
    print("Connexion établie")
    # Envoyer les données
    ws.send(data_json)

# Fonction appelée lorsque les données sont reçues
def on_message(ws, message):
    print("Données reçues:", message)

# Établir une connexion websocket
ws = websocket.WebSocketApp(server_url, on_open=on_open, on_message=on_message)

# Démarrer le thread du client websocket
ws.run_forever()
