# Orif Section Informatique
#
# Exercice 1.5
# Calcul du diamètre et de la circonférence d'un cerle
#
# Auteur:   Lawrence Haesler
# Date:     19.01.2026

import math

print("Orif section informatique - Exercice 1.5 - Lawrence Haesler")
print("Programme qui calcule le diamètre et la circonférence d'un cercle")
print("______________________________")

rayon = float(input("Veuillez indiquer le rayon du cercle : "))
diametre = rayon * 2
circonference = 3.14 * 2 * rayon

# pi can also be accessed via math.pi via: 'import math'
circonference = math.pi * 2 * rayon
# this does however return a float value that is excessively precise
# La circonférence du cercle est de 18.84955592153876 unités

# this is where the round() function is used: round(number, decimalplaces)

circonference = round(circonference, 3) # will round to 3 decimal places

print("Le diametre du cercle est de", diametre, "unités")
print("La circonférence du cercle est de", circonference, "unités")