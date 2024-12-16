# List Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

evens = [number for number in numbers if number % 2 == 0]

evens = [
    number
    for number in numbers
    if number % 2 == 0
]

print(evens)