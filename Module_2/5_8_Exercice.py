# Orif Section Informatique
#
# Exercice 5.8
# Calculer les frais de voyage en cars V3
#
# Auteur:   Lawrence Haesler
# Date:     26.01.2026

import os
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 5.8 - Lawrence Haesler")
print("Calculer les frais de voyage en cars V3")
print("______________________________")

while True:
    kmTotal = float(input(f"{f"Indiquez combien de kilomètres pour un aller simple":<75}: ")) * 2
    joursTotal = int(input(f"{f"Indiquez combien de jours en total (nombres entiers, minimum 1)":<75}: "))
    passagersTotal = int(input(f"{f"Indiquez combien de passagers en total (nombres entiers, minimum 1)":<75}: "))

    if kmTotal <= 0 or joursTotal <= 0 or passagersTotal <= 0:
        print("Veuillez uniquement utiliser des nombres positifs, le nombre de jours et de passagers minimum est de 1")
        continue
    
    kmTotalRetour = kmTotal * 2
    nuitsLogement = joursTotal - 1
    joursImmobile = joursTotal - 2 if joursTotal > 1 else 0

    passagers = passagersTotal
    nbGrandCar = 0
    nbMediumCar = 0
    nbPetitCar = 0

    while passagers > 0:
        if passagers > 50 and nbGrandCar < 3:
            passagers -= 65
            nbGrandCar += 1
        elif passagers > 35 and nbMediumCar < 5:
            passagers -= 50
            nbMediumCar += 1
        elif nbPetitCar < 2:
            passagers -= 35
            nbPetitCar += 1
        else:
            print("Il n'y a pas assez de cars pour ce nombre de passagers")
            exit()

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

    nbTotalCar = nbPetitCar + nbMediumCar + nbGrandCar

    tarifLogement = 100 * nbTotalCar
    tarifImmobile = 300 * nbTotalCar

    fraisDeplacementParCar = tarif * kmTotal
    fraisDeplacementTotal = fraisDeplacementParCar * nbTotalCar
    fraisLogement = nuitsLogement * tarifLogement
    fraisImmobile = joursImmobile * tarifImmobile
    fraisTotalSansRetour = fraisDeplacementTotal + fraisLogement + fraisImmobile

    fraisDeplacementRetourParCar = kmTotalRetour * tarifRetour
    fraisDeplacementRetourTotal = fraisDeplacementRetourParCar * nbTotalCar

    print("\nCars attribués :")
    print("----------------")
    print(f"{nbGrandCar} car(s) de 65 places")
    print(f"{nbMediumCar} car(s) de 50 places")
    print(f"{nbPetitCar} car(s) de 35 places")

    print("\nCalcul des frais en gardant le(s) car(s) sur place :")
    print("----------------------------------------------------")

    print(f"{f"Coût du déplacement par car ({kmTotal} kilomètres à {tarif}.-)":<75}: {fraisDeplacementParCar}")
    print(f"{f"Coût du déplacement total ({nbTotalCar} cars)":<75}: {fraisDeplacementTotal}")
    print(f"{f"Coût de logement des chauffeurs ({nuitsLogement} nuits à {tarifLogement}.-)":<75}: {fraisLogement}")
    print(f"{f"Frais d'immobilisation du car ({joursImmobile} jours à {tarifImmobile}.-)":<75}: {fraisImmobile}")
    print(f"{f"----------":>85}")
    print(f"{f"TOTAL ":>75}: {fraisTotalSansRetour}")
    print("\nCalcul des frais en renvoyant le(s) car(s) :")
    print("--------------------------------------")
    print(f"{f"Coût du déplacement par car ({kmTotalRetour} kilomètres à {tarifRetour}.-)":<75}: {fraisDeplacementRetourParCar}")
    print(f"{f"Coût du déplacement total ({nbTotalCar} cars)":<75}: {fraisDeplacementRetourTotal}")
    print(f"{f"----------":>85}")
    print(f"{f"TOTAL ":>75}: {fraisDeplacementRetourTotal}")

    if input("\nVoulez-vous recommencer (O / N) ? : ").capitalize() != 'O':
        break

    Clear()     # clear console if user restarts


