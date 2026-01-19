# Orif Section Informatique
#
# Exercice 1.1
# Conversion de kilos en tonnes
#
# Auteur:   Lawrence Haesler
# Date:     19.01.2026

print("Orif section informatique - Exercice 1.1 - Lawrence Haesler")
print("Programme qui convertit les kilos en tonnes")
print("______________________________")

# if a float is used as an input here, e.g. 0.03, an error will be thrown
# kilos = int(input("Indiquez le nombre de kilos : "))
# ValueError: invalid literal for int() with base 10: '0.03'

kilos = float(input("Indiquez le nombre de kilos : "))      # this is arguably better
tonnes = kilos / 1000                                       # returns a float value

print("Conversion en tonnes : " + str(tonnes) + " tonnes")