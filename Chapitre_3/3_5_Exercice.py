# Orif Section Informatique
#
# Exercice 3.5
# Programme qui détermine le groupe selon l'âge du scout
#
# Auteur:   Lawrence Haesler
# Date:     20.01.2026

import os
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 3.5 - Lawrence Haesler")
print("Programme qui détermine le groupe selon l'âge du scout")
print("______________________________")

userInput = int(input("Indiquez l'âge du scout : "))

if userInput >= 18 :
    print("Le scout est chef de meute")
elif userInput >= 12 :
    print("Le scout est dans le groupe Scout")
elif userInput >= 7 :
    print("Le scout est dans le groupe Louveteau")
else :
    print("Le scout est dans le goupe Cadets")

# The logic here is actually a little tricky, as you must be very precise with the wording :
# Less than 7 years old => Cadet            therefore 7 is Louveteau
# Less than 12 years old => Louveteau       therefore 12 is Scout
# Less than 18 years old => Scout           therefore 18 is Chef
# 18 or over => Chef de meute

# Logic like this is redundant, as the if block will exit as soon as one of the conditions is met
# if userInput >= 18:
#     print("Le scout est chef de meute")
# elif 18 > userInput >= 12:
#     print("Le scout est dans le groupe Scout")
# elif 12 > userInput >= 7:
#     print("Le scout est dans le groupe Louveteau")
# else 7 > userInput:
#     print("Le scout est dans le goupe Cadets")
