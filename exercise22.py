f = open("hello.txt")

for line in f:
    #print(line.strip())
    print(line, end="")

with open("hello.txt") as f:
    for line in f:
        print(line, end="")