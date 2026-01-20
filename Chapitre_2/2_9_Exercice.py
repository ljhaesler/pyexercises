# Orif Section Informatique
#
# Exercice 2.9
# Programme d'aide à la répétition du livret
#
# Auteur:   Lawrence Haesler
# Date:     20.01.2026

print("Orif section informatique - Exercice 2.9 - Lawrence Haesler")
print("--- Programme d’aide à la répétition du livret ----")
print("---------------------------------------------------")

livret = int(input("Quel livret voulez-vous ? "))
max = int(input("A combien voulez-vous qu'il stoppe ? "))

print("\nVoici le livret", livret, "multiplié jusqu'à", max)
for x in range(1, max + 1):                         # again, + 1 is required to include the max value itself
    print(x, "*", livret, "=", x * livret)