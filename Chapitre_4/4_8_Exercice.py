# Orif Section Informatique
#
# Exercice 4.8
# Programme jeu de nombre avec nombre aléatoire
#
# Auteur:   Lawrence Haesler
# Date:     22.01.2026

import os
import random

Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 4.8 - Lawrence Haesler")
print("Programme jeu de nombre avec nombre aléatoire")
print("______________________________")

nombre = random.randint(1, 100)
nombreChoisi = 0
tentative = 1
bas = 1             # random.randint(1, 50) could also be used here, for example
haut = 100

print("Vous devez trouver un nombre mystérieux entre " + str(bas) + " et " + str(haut) + " !")
while nombre != nombreChoisi:
    nombreChoisi = int(input("Tentative " + str(tentative) + " : "))

    if nombreChoisi == nombre:
        continue

    elif haut >= nombreChoisi > nombre:
        haut = nombreChoisi - 1
        tentative += 1
        print("Le nombre mystérieux se situe entre " + str(bas) + " et " + str(haut) + ".")

    elif bas <= nombreChoisi < nombre:
        bas = nombreChoisi + 1
        tentative += 1
        print("Le nombre mystérieux se situe entre " + str(bas) + " et " + str(haut) + ".")

    else:
        print("Veuillez indiquer un nombre uniquement entre " + str(bas) + " et " + str(haut) + ".")

print("Bravo, vous avez trouvé en", tentative, "tentative(s)!")


# the inverse logic might be clearer :

    # if nombreChoisi == nombre:
    #     continue
    #
    # elif nombreChoisi > haut or nombreChoisi < bas:           -> If the chosen number is greater than or smaller than the max and min, exit early
    #     print("Veuillez indiquer un nombre uniquement entre " + str(bas) + " et " + str(haut) + ".")
    #
    # elif nombreChoisi >= bas:                                 -> If the chosen number is greater than or equal to the minimum, run logic                                      
    #     LOGIC...  
    #
    # elif nombreChoisi =< haut:
    #     LOGIC...
    #     
