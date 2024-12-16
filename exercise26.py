from random import choice
# from random import *      (not recommended)

filename = "names.txt"

with open(filename) as f:
    data = f.read()
    data = data.split("\n")

best = choice(data)
print(f"The best is {best}")