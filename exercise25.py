import random
fruits = [
    "Buko Juice",
    "Guyabano",
    "Apricot",
    "Myrtle",
    "Dragon fruit",
]

best = random.choice(fruits)
power = random.randint(9000, 1_003_000)

print(f"The best fruit is {best}. Its taste is equal to {power}!")