# Exercises should be prepended with the following comments:

# Orif Section Informatique
#
# Exercice X.X
# Description
#
# Auteur:   Lawrence Haesler
# Date:     19.01.2026

largeurPiscine = 14             # implicit coercion to int
salaire = 3000.00               # implicit coercion to float
prenomGrandPere = "Marcel"      # implicit coercion to string

# explicit conversion can be achieved via functions: str(), int(), float()
# these functions are simply known as 'type conversion functions'
# implicit conversion can only occur when no data loss is implied: int + float = float as there will be no loss of precision.

num1 = 55
num2 = 45
res = num1 + num2
res = num1 - num2
res = num1 * num2
res = num1 / num2       # the division operator will always return a float value for ( int / int ), even when there is no remainder
res = num1 ** 2         # power operator

# python allows for basic text concatenation via the + operator as well
text1 = "Hello "
text2 = "World"

final = text1 + text2

print(final)

# print("Test for string concatenation with an int value: " + num1) <- this will not work: TypeError: can only concatenate str (not "int") to str
# the print() and input() functions print and take input from the commandline respectively

# presumably, int() will throw an error if it cannot parse an int
age = int(input("How old are you? "))           # can throw: ValueError: invalid literal for int() with base 10: 'aaa'
print("You are " + str(age))

