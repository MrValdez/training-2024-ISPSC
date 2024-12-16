# DRY: Don't Repeat Yourself

age = int(input("How old are you? "))

if age >= 80 or age <= 0:
    print("That is not a valid age")
elif age >= 18:
    print("You can drive")
else:
    print("You cannot drive yet")
    print("Wait a few years")