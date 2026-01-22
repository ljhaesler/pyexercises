# Orif Section Informatique
#
# Exercice 3.7
# Programme jeu de nombre
#
# Auteur:   Lawrence Haesler
# Date:     20.01.2026

import os
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 3.7 - Lawrence Haesler")
print("Programme jeu de nombre")
print("______________________________")

nombre = None               # it is possible to initialize a value using the None constant
nombreChoisi = 0
tentative = 1


while True:
    nombre = int(input("Indiquez un nombre entre 1 et 100 : "))
    if 100 >= nombre >= 1:
        break
    else:
        print("Veuillez indiquer un nombre uniquement entre 1 et 100")

Clear()

print("Devinez un nombre entre 1 et 100\n")

while nombreChoisi != nombre:
    nombreChoisi = int(input("Tentative " + str(tentative) + " : "))

    if nombreChoisi == nombre:
        continue
    elif 100 >= nombreChoisi > nombre:
        tentative += 1              # note that python does not have a ++ operator
        print("Trop haut")
        continue
    elif 0 <= nombreChoisi < nombre:
        tentative += 1
        print("Trop bas")
        continue
    else:
        print("Veuillez indiquer un nombre uniquement entre 1 et 100")

print("Bravo, vous avez trouvé en", tentative, "tentative(s)!")
