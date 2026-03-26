"""data_structures.py
Basic lists, tuples, sets, and dictionaries."""

# List
fruits = ["apple", "banana", "cherry"]
print("fruits:", fruits)
fruits.append("date")
print("after append:", fruits)
print("first fruit:", fruits[0])

# Tuple (immutable)
colors = ("red", "green", "blue")
print("colors:", colors)

# Set (unique, unordered)
numbers = {1, 2, 3, 2, 1}
print("numbers set:", numbers)
numbers.add(4)
print("numbers after add:", numbers)

# Dictionary
person = {"name": "Alice", "age": 30}
print("person:", person)
print("name:", person["name"])
person["age"] = 31
print("updated person:", person)

# Iterate
print("Iterate fruits:")
for fruit in fruits:
    print("-", fruit)

# Exercise ideas:
# - create a list of 5 items and print each
# - build a dict with favorite foods and print keys/values

