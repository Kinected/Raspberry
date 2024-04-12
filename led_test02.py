import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 115

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False
)

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

while True:
    up_left()
    time.sleep(1)
    shutdown()
    right()
    time.sleep(1)
    shutdown()
    down_left()
    time.sleep(1)
    shutdown()
    down()
    time.sleep(1)
    shutdown()
    down_right()
    time.sleep(1)
    shutdown()
    left()
    time.sleep(1)
    shutdown()
    up_right()
    time.sleep(1)
    shutdown()
    up()
    time.sleep(1)
    shutdown()