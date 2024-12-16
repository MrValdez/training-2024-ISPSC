# while loop

while True:
    print("Pogi/Ganda ako")

    reply = input("Totoo ba? ").lower()

#    if reply == "yes" or reply == "oo":
    if reply in ["yes", "oo", "opo"]:
        break       # works on for loops

    if reply == "hinde":
        print("liar")
        continue    # also works on for loops

    print("Let's go again")

print("Tapos na ang usapan")