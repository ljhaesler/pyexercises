# Orif Section Informatique
#
# Exercice 2.6
# Compte à rebours de 20 à 1 avec temps d'attente
#
# Auteur:   Lawrence Haesler
# Date:     20.01.2026

print("Orif section informatique - Exercice 2.6 - Lawrence Haesler")
print("Programme qui compte à rebours de 20 à 1 avec temps d'attente")
print("______________________________")

import time             # import the time module from the python standard library

for x in range(20, 0, -1):          
    print(x)
    time.sleep(1)  