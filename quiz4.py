# Make a program that asks the user for the first name, last name, and gender
# Loop the asking until the user wish to stop
# Add all the data into a loop
# Using a for loop, print all the data

data = []

running = True
while running:
    fname = input("What is your first name? ").title()
    lname = input("What is your last name? ").title()
    gender = input("What is your gender? ").title()
    data.append([fname, lname, gender])

    if input("Stop (Y/n)?").upper() == "Y":
        running = False
        break

for fname, lname, gender in data:
    print(f"First name: {fname.title()}\nLast name: {lname.title()}\nGender: {gender.title()}")
    print("===")