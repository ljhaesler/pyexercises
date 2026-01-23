# Orif Section Informatique
#
# Exercice 5.5
# Calculer la répartition d'un héritage
#
# Auteur:   Lawrence Haesler
# Date:     23.01.2026

import os
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 5.5 - Lawrence Haesler")
print("Calculer la répartition d'un héritage")
print("______________________________")

conjoint = None
enfants = None
parents = None

montantBrut = float(input("Indiquez le montant brut de l'héritage : "))
montantNet = montantBrut * 0.6 if montantBrut * 0.05 >= 400 else montantBrut * 0.65 - 400

if montantNet < 0:
    print("Le notaire ne peut pas accepter ce travail, il ne recevra pas 400 francs au minimum")
    exit()

conjoint = True if input("Le défunt a un conjoint? ( O / N ) : ").capitalize() == "O" else False
nombreEnfant = int(input("Combien d'enfants a le défunt? : "))
nombreParent = int(input("Combien de parents a le défunt? ( 0 / 1 / 2 ) : "))

if conjoint:
    if nombreEnfant:
        partConjoint = montantNet * 0.5
        partEnfant = montantNet * 0.5 / nombreEnfant
        partParent = 0
    elif nombreParent:
        partConjoint = montantNet * 0.75
        partEnfant = 0
        partParent = montantNet * 0.25
    else:
        partConjoint = montantNet
        partEnfant = 0
        partParent = 0
else:
    if nombreEnfant:
        partConjoint = 0
        partEnfant = montantNet / nombreEnfant
        partParent = 0
    elif nombreParent:
        partConjoint = 0
        partEnfant = 0
        partParent = montantNet / nombreParent
    else:
        print("L'héritage de", montantNet, "partira aux héritiers réservataires.")
        exit()

print("L'héritage net est de", montantNet)
print("Le part pour le conjoint est de", partConjoint, "CHF")
print("Le part pour chaque enfant est de", partEnfant, "CHF")
print("Le part pour chaque parent est de", partParent, "CHF")