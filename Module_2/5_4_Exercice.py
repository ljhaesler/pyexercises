# Orif Section Informatique
#
# Exercice 5.4
# Calculatrice simple
#
# Auteur:   Lawrence Haesler
# Date:     23.01.2026

import os
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 5.4 - Lawrence Haesler")
print("Calculatrice simple")
print("______________________________")

valeurs = []
operateursValide = ["+", "-", "*", "/", "="]

while True:
    nombre = str(float(input("Nombre".ljust(75) + ": ")))
    valeurs.append(nombre)

    operateur = input("Opérateur (+, -, *, /, =)".ljust(75) + ": ")
    while operateur not in operateursValide:
        operateur = input("Veuillez uniquement utiliser les opérateurs suivants: +, -, *, /, =".ljust(75) + ": ")
        continue
    if operateur == '=':
        break

    valeurs.append(operateur)


print("Résultat de {}".format(' '.join(valeurs)).ljust(75) + ":", eval(''.join(valeurs)))