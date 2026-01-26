# Orif Section Informatique
#
# Exercice 5.6
# Calculer les frais de voyage en cars V1
#
# Auteur:   Lawrence Haesler
# Date:     23.01.2026

import os
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 5.6 - Lawrence Haesler")
print("Calculer les frais de voyage en cars V1")
print("______________________________")

# will have to look into f-strings for this kind of justifying/padding
# input(f"{'Indiquez combien de kilomètres pour un aller simple':<75}: ")

# 

while True:
    kmTotal = float(input(f"{f'Indiquez combien de kilomètres pour un aller simple':<75}: ")) * 2
    joursTotal = int(input(f"{f'Indiquez combien de jours en total (nombre entier)':<75}: "))

    if kmTotal < 0 or joursTotal < 0:
        print("Veuillez uniquement utiliser des nombres positifs")
        continue

    nuitsLogement = joursTotal - 1
    joursImmobile = joursTotal - 2

    if kmTotal > 2500:
        tarif = 3
    elif kmTotal > 1000:
        tarif = 4
    elif kmTotal > 500:
        tarif = 5
    else:
        tarif = 6

    fraisDeplacement = tarif * kmTotal
    fraisLogement = nuitsLogement * 100
    fraisImmobile = joursImmobile * 300

    print("Calcul des frais :")
    print("------------------")

    print(f"{f'Coût du déplacement ({kmTotal} kilomètres à {tarif}.-)':<75}: {fraisDeplacement}")
    


