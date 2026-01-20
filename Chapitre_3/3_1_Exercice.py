# Orif Section Informatique
#
# Exercice 3.1
# Programme qui indique si un nombre est supérieur, égal ou inférieur à 50
#
# Auteur:   Lawrence Haesler
# Date:     20.01.2026

import os
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 3.1 - Lawrence Haesler")
print("Programme qui indique si un nombre est supérieur, égal ou inférieur à 50")
print("______________________________")

userInput = float(input("Indiquez un nombre : "))

if userInput > 50:
    print(userInput, "est supérieur à 50")
elif userInput < 50:
    print(userInput, "est inférieur à 50")
else:
    print(userInput, "est égal à 50!")