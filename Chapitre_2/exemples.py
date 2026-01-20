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

# a for loop in Python is written as
for x in range(5):
    print(x)

# range() itself is a built-in function, it returns a 'range' object representing a sequence of integers
# fundamentally it generates a simple iterable that can be used over a for loop
# range(start, stop, step) or simply range(stop), where it ranges from 0 to the stop value over a step value of 1
# a range object for a loop is much more efficient than a list (or other iterable), as a list will store each seperate value in memory, a range will not

print(list(range(1, 11)))           # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(0, 20, 2)))        # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# list() is also a built-in function & type, in python an array and a list are seperate types
# array types must be imported from the standard library, all of its elements must be of the same type, and they are not explicitly dynamically sized
# (they are mutable but reallocation may occur and is less efficient)

from array import array
print(array('i', range(5)))         # array('i', [0, 1, 2, 3, 4])
# a list can contain multiple different types, and can be dynamically resized, much like arrays in JS.

# ranges can also be used to iterate backwards
for y in range(5, 0, -1):
    print(y)

