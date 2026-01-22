# Orif Section Informatique
#
# Exercice 4.1
# Programme qui génère et affiche 100 nombres entiers aléatoires
#
# Auteur:   Lawrence Haesler
# Date:     22.01.2026

import os
import random
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 4.1 - Lawrence Haesler")
print("Programme qui génère et affiche 100 nombres entiers aléatoires")
print("______________________________")

for x in range(1, 100):
    print(x, ":", random.randint(1, 100))