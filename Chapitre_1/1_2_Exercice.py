# Orif Section Informatique
#
# Exercice 1.2
# Conversion de kilos en tonnes
#
# Auteur:   Lawrence Haesler
# Date:     19.01.2026

print("Orif section informatique - Exercice 1.2 - Lawrence Haesler")
print("Programme qui affiche le 5% d'un nombre")
print("______________________________")


# the largest float value is '1.7976931348623157e+308'
nombre = float(input("Indiquez un nombre : "))
cinqPourCent = nombre * 5 / 100

print("Le 5% de " + str(nombre) + " est " + str(cinqPourCent))
# can print: Le 5% de 1.7976931348623157e+308 est inf
# upon multiplication by 5, the number overflows to infinity
# however: cinqPourCent = number / 100 * 5 will work
cinqPourCent = nombre / 100 * 5
print("Le 5% de " + str(nombre) + " est " + str(cinqPourCent))
# returns: Le 5% de 1.7976931348623157e+308 est 8.988465674311578e+306
