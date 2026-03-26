"""functions.py
User-defined functions, parameters, returns, and simple logic."""

# Function without return
def greet():
    print("Hello from greet()")

# Function with parameter
def greet_person(name):
    print(f"Hello, {name}!")

# Function with return value
def add(a, b):
    return a + b

# Function with more logic
def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    greet()
    greet_person("Bob")
    print("add(3, 5) =", add(3, 5))
    print("factorial(5) =", factorial(5))

    # Exercise: create subtract, divide, and pow functions
    # def subtract(a, b):
    #     return a - b
    #
    # def divide(a, b):
    #     return a / b


