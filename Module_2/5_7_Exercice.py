# Orif Section Informatique
#
# Exercice 5.7
# Calculer les frais de voyage en cars V2
#
# Auteur:   Lawrence Haesler
# Date:     26.01.2026

import os
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 5.7 - Lawrence Haesler")
print("Calculer les frais de voyage en cars V2")
print("______________________________")

while True:
    kmTotal = float(input(f"{f"Indiquez combien de kilomètres pour un aller simple":<75}: ")) * 2
    joursTotal = int(input(f"{f"Indiquez combien de jours en total (nombres entiers, minimum 1)":<75}: "))

    if kmTotal <= 0 or joursTotal <= 0:
        print("Veuillez uniquement utiliser des nombres positifs, le nombre de jours minimum est de 1")
        continue
    
    kmTotalRetour = kmTotal * 2
    nuitsLogement = joursTotal - 1
    joursImmobile = joursTotal - 2 if joursTotal > 1 else 0

    if kmTotal > 2500:
        tarif = 3
    elif kmTotal > 1000:
        tarif = 4
    elif kmTotal > 500:
        tarif = 5
    else:
        tarif = 6

    if kmTotalRetour > 2500:
        tarifRetour = 3
    elif kmTotalRetour > 1000:
        tarifRetour = 4
    elif kmTotalRetour > 500:
        tarifRetour = 5
    else:
        tarifRetour = 6

    fraisDeplacement = tarif * kmTotal
    fraisLogement = nuitsLogement * 100
    fraisImmobile = joursImmobile * 300
    fraisAvecRetour = kmTotalRetour * tarifRetour

    print("\nCalcul des frais :")
    print("------------------")

    print(f"{f"Coût du déplacement ({kmTotal} kilomètres à {tarif}.-)":<75}: {fraisDeplacement}")
    print(f"{f"Coût de logement du chauffeur ({nuitsLogement} nuits à 100.-)":<75}: {fraisLogement}")
    print(f"{f"Frais d'immobilisation du car ({joursImmobile} jours à 300.-)":<75}: {fraisImmobile}")
    print(f"{f"----------":>85}")
    print(f"{f"TOTAL ":>75}: {fraisDeplacement + fraisImmobile + fraisLogement}")
    print("\nCalcul des frais en renvoyant le car :")
    print("--------------------------------------")
    print(f"{f"Coût du déplacement ({kmTotalRetour} kilomètres à {tarifRetour}.-)":<75}: {fraisAvecRetour}")
    print(f"{f"----------":>85}")
    print(f"{f"TOTAL ":>75}: {fraisAvecRetour}")

    if input("\nVoulez-vous recommencer (O / N) ? : ").capitalize() != 'O':
        break

    Clear()     # clear console if user restarts


