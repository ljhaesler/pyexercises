# Orif Section Informatique
#
# Exercice 3.2
# Programme qui compte de 1 à 100 et s'interrompt sur un chiffre préalablement demandé
#
# Auteur:   Lawrence Haesler
# Date:     20.01.2026

import os
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 3.2 - Lawrence Haesler")
print("Programme qui compte de 1 à 100 et s'interrompt sur un chiffre préalablement demandé")
print("______________________________")

userInput = int(input("Indiquez un nombre : "))

for x in range(1, 100):
    print(x)
    if x == userInput:
        break

