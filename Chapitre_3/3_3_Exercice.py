# Orif Section Informatique
#
# Exercice 3.3
# Programme qui demande l’âge d’une personne et indique si elle est majeure ou mineure
#
# Auteur:   Lawrence Haesler
# Date:     20.01.2026

import os
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 3.3 - Lawrence Haesler")
print("Programme qui demande l’âge d’une personne et indique si elle est majeure ou mineure")
print("______________________________")

userAge = int(input("Indiquez votre age : "))

if userAge >= 18:
    print("Vous avez", userAge, "ans et vous êtes majeure")
else:
    print("Vous avez", userAge, "ans et vous êtes mineure")