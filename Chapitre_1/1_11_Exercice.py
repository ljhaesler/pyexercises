# Orif Section Informatique
#
# Exercice 1.11
# Afficher bienvenue
#
# Auteur:   Lawrence Haesler
# Date:     20.01.2026

print("Orif section informatique - Exercice 1.11 - Lawrence Haesler")
print("Programme qui demande un prénom et un nom, pour afficher ensuite 'Bonjour Prenom Nom'")
print("______________________________")

prenom = input("Veuillez indiquer votre prénom : ")     # input should always return a string
nom = input("Veuillez indiquer votre nom : ")           

print("Bonjour " + prenom + " " + nom)                  # string concatenation was explicitly asked for