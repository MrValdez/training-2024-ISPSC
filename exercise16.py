# data type: Dictionary (Dict)
#     key-value storage

row = {
    "First name": "<your first name>",
    "Last name": "<your last name>",
    "Favorite food": ["a", "b", "c"],
}

print(row)
print(type(row))
print(row["First name"])

row["Hobbies"] = ["1", "2"]
print(row["Hobbies"])

print(row.get("First name"))

print(row.get("Motto"))
print(row.get("Motto", "World peace!"))
