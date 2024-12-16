fruits = []

fruits.append("Apple")
#fruits.remove("banana")

fruits[0] = "apple"
fruits.remove("apple")

#fruits[1] = "banana"
fruits.append("banana")
print(fruits)

print("banana" not in fruits)
print("carrot" in fruits)
