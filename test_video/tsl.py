# -*- coding: utf-8 -*-

import time
import board
from adafruit_tsl2561 import TSL2561



# Initialisation du capteur TSL2561
i2c = board.I2C()  # Cr�e l'objet I2C
tsl2561 = TSL2561(i2c)

while True:
    try:
        # Lecture du DHT11
        # Lecture du TSL2561
        lumiere = tsl2561.lux

        # Affichage des valeurs sur la m�me ligne
        if lumiere is not None:
            print(f"{lumiere:.1f}lux")
        else:
            print("Erreur de lecture des capteurs")

    except RuntimeError as error:
        # Gestion des erreurs de lecture des capteurs
        print(error.args[0])

    except Exception as error:
        print(error)
        break  # Sortie de la boucle en cas d'erreur autre que RuntimeError

    time.sleep(1)  # Delai avant la prochaine lecture