# Orif Section Informatique
#
# Exercice 4.3
# Programme qui génère 2 nombres aléatoires entier, puis exécute des calculs
#
# Auteur:   Lawrence Haesler
# Date:     22.01.2026

import os
import random
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 4.3 - Lawrence Haesler")
print("Programme qui génère 2 nombres aléatoires entier, puis exécute des calculs")
print("______________________________")

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

print("Les numéros sont :", num1, "et", num2)
print("Somme".ljust(18), num1, "+", num2, "=", num1 + num2)
print("Différence".ljust(18), num1, "-", num2, "=", num1 - num2)
print("Produit".ljust(18), num1, "*", num2, "=", num1 * num2)
print("Quotient".ljust(18), num1, "/", num2, "=", round(num1 / num2, 3))