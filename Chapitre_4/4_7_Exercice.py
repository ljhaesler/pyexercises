# Orif Section Informatique
#
# Exercice 4.7
# Programme qui génère un nombre aléatoire entre 1 et 100 et qui indique si ce nombre est pair ou impair.
#
#
# Auteur:   Lawrence Haesler
# Date:     22.01.2026

import os
import random
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 4.7 - Lawrence Haesler")
print("Programme qui génère un nombre aléatoire entre 1 et 100 et qui indique si ce nombre est pair ou impair.")
print("______________________________")


num = random.randint(1, 100)
print("Le numéro généré est :", num, "=> ce numéro est", "impair" if bool(num % 2) else "pair")

# note the syntax of a ternary operator in python
# bool(num % 2) ? "impair" : "pair" doesn't exist

# => simply, bool(num % 2) will return false if the remainder is 0 => pair
#                               return true if the remainder is 1 => impair