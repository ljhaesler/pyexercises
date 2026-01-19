# Orif Section Informatique
#
# Exercice 1.8
# Calcul d'horaires
#
# Auteur:   Lawrence Haesler
# Date:     19.01.2026

print("Orif section informatique - Exercice 1.8 - Lawrence Haesler")
print("Programme qui calcule les horaires d'un employé")
print("______________________________")

arrivee = float(input("Indiquez votre heure d'arrivée : "))
depart = float(input("Indiquez votre heure de départ : "))
pauseMidi = float(input("Indiquez la durée de votre pause de midi : "))

# assuming all inputs are in 24 hour time => 8h30 is 8.5, 16h30 is 16.5, 30 minutes break is 0.5...
taux = ( depart - arrivee - pauseMidi) * 5

print("Le taux horaire total est égal à :", taux)