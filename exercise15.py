# unpacking

numbers = [
    ["one",],
    ["two", 2],
    ["three", 3],
]

template = "The text \"{}\" is equal to {}"

for number in numbers:
    text = number[0]
    value = number[1]

    output = template.format(text, value)
    print(output)

print("======")

for number in numbers:
    text, value = number

    output = template.format(text, value)
    print(output)

print("======")

for text, value in numbers:
    output = template.format(text, value)
    print(output)
