# Orif Section Informatique
#
# Exercice 1.9
# Calcul salaire net
#
# Auteur:   Lawrence Haesler
# Date:     19.01.2026

print("Orif section informatique - Exercice 1.9 - Lawrence Haesler")
print("Programme qui calcule le salaire net")
print("______________________________")

avs = 4.2 
ai = 0.7
apg = 0.25
ac = 1
anp = 1.3
lpp = 7

salaireBrut = float(input("Indiquez le salaire brut : "))
salaireNet = salaireBrut * ( 1 - (avs + ai + apg + ac + anp + lpp) / 100 )

print("Le salaire net est égale à :", salaireNet)
