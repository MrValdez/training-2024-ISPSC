# Take your quiz4. Instead of appending a list,
# use a dictionary instead.

data = []

running = True
while running:
    fname = input("What is your first name? ").title()
    lname = input("What is your last name? ").title()
    gender = input("What is your gender? ").title()
    row = {
        "First name": fname,
        "Last name": lname,
        "Gender": gender,
    }
    data.append(row)

    if input("Stop (Y/n)?").upper() == "Y":
        running = False
        break

for row in data:
    for key, value in row.items():
        print(f"{key}: {value}")