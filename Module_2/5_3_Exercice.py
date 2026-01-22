# Orif Section Informatique
#
# Exercice 5.3
# Programme qui calcule la moyenne des notes des élèves
#
# Auteur:   Lawrence Haesler
# Date:     22.01.2026

import os
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 5.3 - Lawrence Haesler")
print("Programme qui calcule la moyenne des notes des élèves")
print("______________________________")

notes = []
continuer = 'O'

while continuer == 'O':
    note = float(input("Indiquez une note (indiquez 0 pour calculer la moyenne): "))

    if note != 0:
        notes.append(note)
        continue
    
    if len(notes) == 0:
        print("Vous devez indiquer au moins une note pour caluler une moyenne.")
        continue

    resultat = sum(notes) / len(notes)          # sum() will simply sum the values of an iterables items

    print("La moyenne finale est de :", resultat)
    continuer = input("Souhaitez vous continuer? ( O / N ) : ").capitalize()           # capitalize for either 'o' or 'O' as input
    notes = []                                                                         # resetting the notes list is necessary, otherwise old values will remain...
    

