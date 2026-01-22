# Orif Section Informatique
#
# Exercice 4.2
# Programme qui génère et affiche 100 nombres décimaux aléatoires
#
# Auteur:   Lawrence Haesler
# Date:     22.01.2026

import os
import random
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 4.2 - Lawrence Haesler")
print("Programme qui génère et affiche 100 nombres décimaux aléatoires")
print("______________________________")

for x in range(1, 100):
    print(x, ":", round(random.random(), 3))
