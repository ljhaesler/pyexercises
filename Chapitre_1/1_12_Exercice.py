# Orif Section Informatique
#
# Exercice 1.12
# Calcul fiche de salaire
#
# Auteur:   Lawrence Haesler
# Date:     20.01.2026

print("Orif section informatique - Exercice 1.12 - Lawrence Haesler")
print("Programme qui génère une fiche de salaire détaillée")
print("______________________________")

avs = 4.2 
ai = 0.7
apg = 0.25
ac = 1
anp = 1.3
lpp = 7

prenom = input("\nVeuillez indiquer votre prénom : ")     
nom = input("Veuillez indiquer votre nom : ")    
metier = input("Indiquez votre métier : ")
naissance = input("Indiquez votre date de naissance : ")
salaireBrut = float(input("Indiquez votre salaire mensuel brut : "))

salaireNet = salaireBrut * ( 1 - (avs + ai + apg + ac + anp + lpp) / 100 )
salaireAnnuelNet = salaireNet * 12
totalDeductions = salaireBrut * (avs + ai + apg + ac + anp + lpp) / 100

print("\n-------------------------------------------------------------------")
# mix of string concetenation and multiple arguments for consistent whitespace
print("Fiche de salaire de", prenom, nom + ", " + metier + ",", "né le", naissance)
print("-------------------------------------------------------------------")
print("\nSalaire mensuel brut :", salaireBrut)
print("\nDéductions :")
print("- AVS (" + str(avs) + "%)  :", round(avs / 100 * salaireBrut, 2))          # floating point arithmetic cannot always calculate floats correctly, so round() is necessary
print("- AI (" + str(ai) + "%)    :", round(ai / 100 * salaireBrut, 2))           # => - AI (0.7%)  : 384.99999999999994 isn't correct
print("- APG (" + str(apg) + "%)  :", round(apg / 100 * salaireBrut, 2))
print("- AC (" + str(ac) + "%)    :", round(ac / 100 * salaireBrut, 2))
print("- ANP (" + str(anp) + "%)  :", round(anp / 100 * salaireBrut, 2))
print("- LPP (" + str(lpp) + "%)  :", round(lpp / 100 * salaireBrut, 2))
print("----------------------------------")
print("Total des déductions : ", totalDeductions)
print("----------------------------------")
print("Salaire net          : ", salaireNet)
print("==================================")
print("Salaire net annuel   : ", salaireAnnuelNet)