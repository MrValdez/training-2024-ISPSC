import random

filename = "names.txt"

with open(filename) as f:
    data = f.read()
    data = data.split("\n")

random.shuffle(data)

for i, line in enumerate(data):
    print(f"#{i + 1}: {line}")

    i += 1
    print(f"#{i}: {line}")
