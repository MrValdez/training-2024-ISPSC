# list slicing

fruits = [
    "Buko Juice",  # 0
    "Guyabano",    # 1 
    "Apricot",     # 2
    "Myrtle",      # 3
    "Dragon fruit",# 4
]

print(fruits)

sample = fruits[0:3]
print(sample)

# list[start:end:step]
print(fruits[0:3])
print(fruits[3:len(fruits)])
print(fruits[0:len(fruits):2])  # for (int i=0; i < fruits.len; i+=2)

print(fruits[:3])       # top 3
print(fruits[3:])
print(fruits[::2])

print(fruits[-3:])      # bottom 3
print(fruits[:-3])
print(fruits[::-1])

# 3:00