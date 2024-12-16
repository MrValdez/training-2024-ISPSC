# list comprehension

fruits = ["Banana", "Starfruit", "Strawberry",]

fruits2 = []
for fruit in fruits:
    fruits2.append(fruit.upper())

fruits2 = [fruit.upper() for fruit in fruits]

print(fruits2)
