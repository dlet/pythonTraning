"""variables.py
Simple variable declaration and basic operations."""

# Number types
x = 10  # int
pi = 3.14  # float

# String
name = "Alice"

# Boolean
is_student = True

# Print values
print("x =", x)
print("pi =", pi)
print("name =", name)
print("is_student =", is_student)

# Basic arithmetic
sum_value = x + pi
print("sum_value =", sum_value)

# Reassign variables
x = 20
print("x after update =", x)

# Type conversion
float_x = float(x)
int_pi = int(pi)
print("float_x =", float_x, "type:", type(float_x))
print("int_pi =", int_pi, "type:", type(int_pi))

# String formatting
print(f"{name} has x={x}, pi={pi}, student={is_student}")
