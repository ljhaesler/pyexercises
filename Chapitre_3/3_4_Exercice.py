# Orif Section Informatique
#
# Exercice 3.4
# Programme qui demande si vous avez faim
#
# Auteur:   Lawrence Haesler
# Date:     20.01.2026

import os
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 3.4 - Lawrence Haesler")
print("Programme qui demande si vous avez faim")
print("______________________________")


while True:
    userInput = input("Avez-vous faim (o/n)? ")
    if userInput == "o":
        print("La cafétéria est au rez-de-chaussée")
        break
    elif userInput == "n":
        print("Alors je ne peux rien faire pour vous")
        break
    else:
        print("Veuillez répondre par (o) ou (n) svp")
    
