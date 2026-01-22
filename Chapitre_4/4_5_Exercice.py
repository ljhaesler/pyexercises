# Orif Section Informatique
#
# Exercice 4.5
# Programme qui génère 2 nombres aléatoires entiers entre 1 et 100 jusqu'à ce que les deux nombres sont identiques
#
#
# Auteur:   Lawrence Haesler
# Date:     22.01.2026

import os
import random
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 4.5 - Lawrence Haesler")
print("Programme qui génère 2 nombres aléatoires entiers entre 1 et 100 jusqu'à ce que les deux nombres sont identiques")
print("______________________________")

generation = 1
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

print("Génération", generation, ":", num1, "et", num2)

while num1 != num2:
    generation += 1
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print("Génération", generation, ":", num1, "et", num2)

print("Trouvé après", generation, "générations")
    