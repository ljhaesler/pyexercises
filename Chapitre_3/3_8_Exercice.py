# Orif Section Informatique
#
# Exercice 3.8
# Programme jeu de nombre améliorée
#
# Auteur:   Lawrence Haesler
# Date:     20.01.2026

import os
import sys                                                          # importing the argparse package allows for more extensive use of argv[]

Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 3.8 - Lawrence Haesler")
print("Programme jeu de nombre améliorée")
print("______________________________")

nombre = None
nombreChoisi = 0
tentative = 1

bas = int(sys.argv[1]) if len(sys.argv) > 1 else 1                   # int(sys.argv[1]) will throw an error if a string is input
haut = int(sys.argv[2]) if len(sys.argv) > 2 else 100                # Program can now be called via: py FILENAME.py HIGHINT LOWINT

while True:
    nombre = int(input("Veuillez indiquer un nombre entre " + str(bas) + " et " + str(haut) + " : "))
    if bas <= nombre <= haut:
        break
    else:
        print("Veuillez indiquer un nombre uniquement entre " + str(bas) + " et " + str(haut) + ".")

Clear()

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
