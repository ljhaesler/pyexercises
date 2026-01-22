# Orif Section Informatique
#
# Exercice 5.2
# Programme qui converti un paquet de minutes en jours, heures et solde de minutes.
#
# Auteur:   Lawrence Haesler
# Date:     22.01.2026

import os
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 5.2 - Lawrence Haesler")
print("Programme qui converti un paquet de minutes en jours, heures et solde de minutes.")
print("______________________________")

# minutes = None is unnecessary

while True:
    # ! --------- !
    # this minutes variable is actually not scoped to the while block
    # ! --------- !
    minutes = int(input("Veuillez indiquer un nombre de minutes : "))   
    if minutes > 0:
        break
    else:
        print("Le nombre doit être un nombre entier positif")

joursFinal = minutes // 1440
heuresFinal = (minutes % 1440) // 60
minutesFinal = minutes % 60

print(minutes, "minutes est egal à :", joursFinal, "jour(s),", heuresFinal, "heure(s) et", minutesFinal, "minute(s).")
