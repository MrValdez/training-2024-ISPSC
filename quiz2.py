# Make a program that changes all the text from the list
# into upper case. A variable should have all the
# new upper case data. Use for loops and str.upper()

fruits = [
    "Banana",
    "Starfruit",
    "Strawberry",
]

fruits2 = []

for fruit in fruits:
    fruits2.append(fruit.upper())

fruits = fruits2
print(fruits)
