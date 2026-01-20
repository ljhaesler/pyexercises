# Orif Section Informatique
#
# Exercice 1.10
# Calcul devis carrelage
#
# Auteur:   Lawrence Haesler
# Date:     20.01.2026

print("Orif section informatique - Exercice 1.10 - Lawrence Haesler")
print("Programme qui calcule le devis de pose de carrelage, murs inclus")
print("______________________________")

longueur = float(input("Indiquez la longueur de la surface : "))
largeur = float(input("Indiquez la largeur de la surface : "))
profondeur = float(input("Indiquez la profondeur de la surface : "))
prix = float(input("Indiquez le prix au mètre carré du carrelage : "))

surfaceSol = longueur * largeur
surfaceMur1 = profondeur * largeur * 2
surfaceMur2 = profondeur * longueur * 2

surfaceTotal = surfaceMur1 + surfaceMur2 + surfaceSol
prixTotal = surfaceTotal * prix

print("Pour", surfaceTotal, "mètres carré de carrelage, on devra payer", prixTotal)

