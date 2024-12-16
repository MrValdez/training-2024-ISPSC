def greet(name, favorite_fruit="Apple", age=19):
    print("Hello " + name)
    print("You like " + favorite_fruit)
    print(f"You are {age} years old")

def add(a, b):
    return a + b

def main():
    ret = greet("<your name>")
    print(ret)

    greet("<your name>", "Banana")
    greet("<your name>", age=21)
    greet(age=20, name="<your name>", favorite_fruit="Dalandan") # kwargs

    c = add(1, 1)
    print(c)

# dunder / double underscore
if __name__ == "__main__":
    main()