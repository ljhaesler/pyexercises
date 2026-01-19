# Orif Section Informatique
#
# Exercice 1.6
# Calcul du diamètre, de la circonférence, et de la surface d'un cerle
#
# Auteur:   Lawrence Haesler
# Date:     19.01.2026

import math

print("Orif section informatique - Exercice 1.6 - Lawrence Haesler")
print("Programme qui calcule le diamètre, la circonférence, et la surface d'un cercle")
print("______________________________")

rayon = float(input("Veuillez indiquer le rayon du cercle : "))
diametre = rayon * 2
circonference = round(math.pi * 2 * rayon, 3)
surface = round(math.pi * rayon ** 2, 3)        # PEMDAS should take precedence and the power operator should always run first

print("Le diametre du cercle est de", diametre, "unités")
print("La circonférence du cercle est de", circonference, "unités")
print("La surface du cercle est de", surface, "unités")