import time
import board
import neopixel
import websocket
import json

# URL du serveur websocket sur la Raspberry Pi
server_url = "ws://172.20.10.6:8000/ws/swipes"

# Choix d'un pin ouvert connecté à l'entrée de données de la bande NeoPixel, par exemple board.D18
pixel_pin = board.D18

# Nombre de NeoPixels
num_pixels = 115
intensity = 55
switch = False

# Configuration des NeoPixels
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)

def up_left():
    for i in range(0, 5):
        pixels[i] = (255, 255, 255)
    for i in range(110, 115):
        pixels[i] = (255, 255, 255)
    pixels.show()

def right():
    for i in range(13, 23):
        pixels[i] = (255, 255, 255)
    pixels.show()

def down_left():
    for i in range(31, 41):
        pixels[i] = (255, 255, 255)
    pixels.show()

def down():
    for i in range(41, 51):
        pixels[i] = (255, 255, 255)
    pixels.show()

def down_right():
    for i in range(52, 62):
        pixels[i] = (255, 255, 255)
    pixels.show()

def left():
    for i in range(70, 80):
        pixels[i] = (255, 255, 255)
    pixels.show()

def up_right():
    for i in range(89, 99):
        pixels[i] = (255, 255, 255)
    pixels.show()

def up():
    for i in range(99, 109):
        pixels[i] = (255, 255, 255)
    pixels.show()

def shutdown():
    pixels.fill((0, 0, 0))
    pixels.show()

def hover_select(data):
    if data['action'] == 'hover_down-right':
        up_left()
    if data['action'] == 'hover_right':
        left()
    if data['action'] == 'hover_up-right':
        down_left()
    if data['action'] == 'hover_down':
        up()
    if data['action'] == 'hover_down-left':
        up_right()
    if data['action'] == 'hover_left':
        right()
    if data['action'] == 'hover_up-left':
        down_right()
    if data['action'] == 'hover_up':
        down()

# Fonction appelée lorsque la connexion websocket est ouverte
def on_open(ws):
    print("Connexion établie")

# Fonction appelée lors de la réception de données via websocket
def on_message(ws, message):
    global intensity
    global switch
    try:
        # Analyser les données JSON reçues
        data = json.loads(message)
        print("Données reçues:", data)
        if data['hand'] is None:
            if switch == True:
                switch = False
            if intensity > 55:
                intensity = intensity - 50
            pixels.fill((intensity, intensity, intensity))
            pixels.show()
        else:
            if intensity < 255 and switch == False:
                intensity = intensity + 50
            if intensity == 255:
                switch = True
            if switch == True and intensity > 105:
                intensity = intensity - 50
            pixels.fill((intensity, intensity, intensity))
            pixels.show()
        if data['action'] == 'click':
            pixels.fill((0, 255, 0))
            pixels.show()
            time.sleep(0.5)
            pixels.fill((intensity, intensity, intensity))
            pixels.show()
        if data['action'] == 'up' or data['action'] == 'down' or data['action'] == 'left' or data['action'] == 'right' or data['action'] == 'up-left' or data['action'] == 'up-right' or data['action'] == 'down-left' or data['action'] == 'down-right':
            pixels.fill((0, 0, 255))
            pixels.show()
            time.sleep(0.5)
            pixels.fill((intensity, intensity, intensity))
            pixels.show()
        hover_select(data)
        
            
    except Exception as e:
        print("Erreur lors du traitement des données:", e)

# Fonction pour se connecter au serveur websocket
def connect_to_websocket():
    print("Tentative de connexion au serveur websocket...")
    ws = websocket.WebSocketApp(server_url, on_open=on_open, on_message=on_message)
    ws.run_forever()

# Boucle pour essayer de se reconnecter toutes les 5 secondes
while True:
    try:
        connect_to_websocket()
    except Exception as e:
        print("Erreur lors de la connexion au serveur websocket:", e)
    time.sleep(5)
