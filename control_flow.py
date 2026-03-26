"""control_flow.py
If/else and loops examples."""

temperature = 22

if temperature > 30:
    print("It's hot today.")
elif temperature > 20:
    print("Nice weather.")
else:
    print("It's cool or cold.")

# For loop
print("for loop 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# While loop
print("while loop counting down 5 to 1:")
n = 5
while n > 0:
    print(n, end=" ")
    n -= 1
print()

# break / continue
print("even numbers up to 10:")
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i, end=" ")
print()

# Exercise to try:
# for i in range(1, 11):
#     if i == 7:
#         break
#     print(i)

