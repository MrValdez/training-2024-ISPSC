row = {
    "First name": "<your first name>",
    "Last name": "<your last name>",
    "Favorite food": ["a", "b", "c"],
}

for key in row:
    print(key)

print ("===")

for value in row.values():
    print(value)

print ("===")

for key, value in row.items():
    #print(key, value)
    print(f"{key=} {value=}")