name = input("What is your name? ")
age = int(input("How old are you? "))

output = "You are" + name + ". You are " + str(age) + "years old"

# string formatting operator %
output = "You are %s. You are %i years old" % (name, age)

# string formatting
output = "You are {}. You are {} years old".format(name, age)

# f-string
output = f"You are {name}. You are {age} years old"

print(output)