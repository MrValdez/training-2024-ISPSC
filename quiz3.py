# Make a program that extracts all even numbers.
# Put the even numbers in a list
# Use for loops and %
#  Examples: 1 % 2 == 1
#            6 % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print(evens)