# Orif Section Informatique
#
# Exercice 1.3
# Calcule de la surface d'un rectangle
#
# Auteur:   Lawrence Haesler
# Date:     19.01.2026

print("Orif section informatique - Exercice 1.3 - Lawrence Haesler")
print("Programme qui calcule la surface d'un rectangle")
print("______________________________")

# input always returns a string
largeur = float(input("Indiquez la largeur du rectangle : "))
longueur = float(input("Indiquez la longueur du rectangle : "))

surface = longueur * largeur

# print will coerce everything into a string, but string concatenation is a separate operation

# print("La surface du rectangle est de " + str(surface) + " unités") # without str(surface) an error will be thrown.
print("La surface du rectangle est de", surface, "unités")

# both of these will work, print will add whitespace between each coerced argument automatically.

