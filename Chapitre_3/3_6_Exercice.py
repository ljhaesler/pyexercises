# Orif Section Informatique
#
# Exercice 3.6
# Programme qui détermine le groupe automobile de certaines marques
#
# Auteur:   Lawrence Haesler
# Date:     20.01.2026

import os
Clear = lambda : os.system("cls")
Clear()

print("Orif section informatique - Exercice 3.6 - Lawrence Haesler")
print("Programme qui détermine le groupe automobile de certaines marques")
print("______________________________")

userInput = input("Indiquez un nom de marque : ").lower()           # here we can use a method on the string standard type to set all chars to lowercase.

gm = ["volvo", "ford", "fiat", "opel"]                              # the [...] syntax declares a list type
vag = ["vw", "audi", "skoda", "seat"]
psa = ["peugeot", "citroën", "citroen"]
gr = ["renault", "nissan"]

if userInput in gm:                                                 # notice how this uses the 'in' operation, like the for loop => for x in [1,2,3,4,5]
    print("Cette marque appartient à General Motors")               # there is also a 'not in' operation => if userInput not in gm:
elif userInput in vag:                                              # as far as I can tell, the in operation can be run on any basic sequence type :
    print("Cette marque appartient à VAG")                          # list [], tuple (), and range
elif userInput in psa:                                              # it can also be run on a string value : "gg" in "eggs"
    print("Cette marque appartient à PSA")                          # a tuple is by definition immutable and heterogeneous
elif userInput in gr:                                               # a list is by definition mutable and conventionally homogeneous, but not necessarily so
    print("Cette marque appartient au Groupe Renault")
else:
    print("Je ne reconnais pas cette marque")

# if userInput == ("volvo" or "ford" or "fiat" or "opel"):            # note that the | operator refers to the bitwise OR, and || does not exist
#     print("Cette marque appartient à General Motors")               # also notably, neither of these will work :
# elif userInput == ("vw" or "audi" or "skoda" or "seat"):            # userInput == ("volvo" or "ford" or "fiat" or "opel")
#     print("Cette marque appartient à VAG")                          # userInput == "volvo" or "ford" or "fiat" or "opel"
# elif userInput == ("peugeot" or "citroën" or "citroen"):            # in the first context, userInput will never == ("volvo" or "ford" or "fiat" or "opel")
#     print("Cette marque appartient à PSA")                          # and in the second, userInput == "volvo" will be checked, but 'or "ford"' will always resolve to true
# elif userInput == ("renault" or "nissan"):                          # essentially : bool((userInput = "volvo") || "ford") always resolves to true.
#     print("Cette marque appartient au Groupe Renault")              # a verbose option would be : if userInput == "volvo" or userInput == "ford" or ...
# else :                                                              # so instead I would recommend using a list
#     print("Je ne reconnais pas cette marque")