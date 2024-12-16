# f = open("hello.txt", "r")
f = open("hello.txt")
data = f.read()
f.close()
print(data)

with open("hello.txt") as f:
    data = f.read()

print(data)