# data type: tuple (an iterable)

heroes = ("Jose Rizal", "Andres Bonifacio", "Kardo Dalisay",)
#heroes = ("Jose Rizal")     # not a tuple
heroes = ("Jose Rizal",)     # for 1 element tuples, comma is required

print(heroes)
print(type(heroes))
print(len(heroes))
print(heroes[1])

heroes = list(heroes)
heroes.remove("Kardo Dalisay")
