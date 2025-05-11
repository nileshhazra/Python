def greet():
    print("hello")


greet()


def add(a, b):
    return a + b


result = add(10, 20)
print(result)


def add5(a, b=5):
    return a + 5


print(add5(10))


def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


introduce(age=25, name="Alice")


# variable length arguments
def print_numbers(*args):
    for num in args:
        print(num)


print_numbers(1, 2, 3, 4)


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Alice", age=25)
