# Orif Section Informatique
#
# Exercice 2.4
# Afficher les nombres de 34 à un nombre choisi avec un pas choisi
#
# Auteur:   Lawrence Haesler
# Date:     20.01.2026

print("Orif section informatique - Exercice 2.4 - Lawrence Haesler")
print("Programme qui affiche les nombres de 34 à un nombre choisi avec un pas choisi")
print("______________________________")

valeur = int(input("Indiquez quand vous souhaitez arrêter le compteur : ")) + 1
pas = int(input("Indiquez avec quel pas vous souhaitez compter : "))
# + 1 is necessary, the number that is input will not be included otherwise

for x in range(34, valeur, pas):               
    print(x)