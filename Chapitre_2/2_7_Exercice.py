# Orif Section Informatique
#
# Exercice 2.7
# Compte à rebours de 20 à 1 avec temps d'attente et explosion
#
# Auteur:   Lawrence Haesler
# Date:     20.01.2026

print("Orif section informatique - Exercice 2.7 - Lawrence Haesler")
print("Programme qui compte à rebours de 20 à 1 avec temps d'attente et explosion")
print("______________________________")

import time             # import the time module from the python standard library
import winsound         # import the winsound module from the python standard library

for x in range(10, 0, -1):          
    print(x)
    time.sleep(1)  

winsound.PlaySound("./explosion.wav", winsound.SND_FILENAME)    # SND_FILENAME indicates that the expected file is a .wav file