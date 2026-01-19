# Orif Section Informatique
#
# Exercice 1.7
# Calcul d'intérêt
#
# Auteur:   Lawrence Haesler
# Date:     19.01.2026

print("Orif section informatique - Exercice 1.7 - Lawrence Haesler")
print("Programme qui calcule l'intérêt d'une somme d'argent, selon un taux et une durée.")
print("______________________________")

somme = float(input("Indiquez une somme d'argent : "))
taux = float(input("Indiquez un taux d'intérêt (pourcentage) : "))
duree = float(input("Indiquez la durée du placement en années : "))

interetNonCumule = somme * taux / 100 * duree

# the actual sum would be equal to => ( somme * (1 + taux / 100) ** duree )
# this assumes the interest is calculated once a year
# => exponential function of form f(x) = a * b^x 
# x in unit years 
# a = some initial value
# b = some ratio
sommeCumule = somme * (1 + taux / 100) ** duree

print("L'intérêt non-cumulé est égale à :", interetNonCumule)
print("La somme cumulé est égale à :", sommeCumule)