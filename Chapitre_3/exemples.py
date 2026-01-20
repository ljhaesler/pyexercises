# Orif Section Informatique
#
# Exercice X.X
# Description
#
# Auteur:   Lawrence Haesler
# Date:     20.01.2026

# print("Orif section informatique - Exercice X.X - Lawrence Haesler")
# print("Programme qui...")
# print("______________________________")


# conditional blocks in python follow a simple structure
# while/if CONDITION:
#       -> run this code

x = 10

while x == 10:
    break                   # break is usable inside loops, as is continue

if x == 10:
    pass                    # pass can be used here, but break/continue requires a loop, return requires a function
elif x == 15:
    pass
else:
    pass

# lambda functions operate the same way as arrow functions in JS, but only one expression can be defined for it (no execution block with () => { ... })
import os                                      # this will import the os module from the python standard library
Clear = lambda : os.system("cls")              # os.system() will run the given command inside of a subshell
Clear()
# => Clear() will simply run 'cls' inside of a subshell to clear the terminal python is running in 

# arguments can be defined for the functon as follows :
Multiply = lambda a, b : a * b
print(Multiply(5, 10))


# in the same way python has some built-in functions, it also has a few built-in constants
# there are: True, False, None, NotImplemented, Ellipsis, __debug__
# there is also a site module with a few more constants that is imported automatically during startup, unless py is called with a -S flag

while True:         # a constant representing the 'True' value of a boolean type
    break

while False:        # a constant representing the 'False' value of a boolean type
    break           # will never run
