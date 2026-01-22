# Orif Section Informatique
#
# Exercice 4.4
# Programme qui génère 2 nombres aléatoires entier, puis exécute des calculs, mais num2 doit être plus petit ou égal à num1
#
# Auteur:   Lawrence Haesler
# Date:     22.01.2026

import os
import random
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 4.4 - Lawrence Haesler")
print("Programme qui génère 2 nombres aléatoires entier, puis exécute des calculs, mais num2 doit être plus petit ou égal à num1")
print("______________________________")

num1 = random.randint(1, 100)
num2 = random.randint(1, num1)

print("Les numéros sont :", num1, "et", num2)                                       # str.ljust(width, fillchar)
print("Somme".ljust(18), num1, "+", num2, "=", num1 + num2)                         # can be used to justify any string to a given width value
print("Différence".ljust(18), num1, "-", num2, "=", num1 - num2)                    # default fillchar is ' '
print("Produit".ljust(18), num1, "*", num2, "=", num1 * num2)
print("Quotient".ljust(18), num1, "/", num2, "=", round(num1 / num2, 3))