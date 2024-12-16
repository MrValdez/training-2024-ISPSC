f = open("hello.txt", "a")
f.write("Good afternoon\n")
f.write("\n")
f.close()

with open("hello.txt", "a") as f:
    f.write("Good afternoon\n")
    f.write("\n")