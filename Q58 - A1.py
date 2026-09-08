# Find GCD / HCF of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b
while y != 0:
    x, y = y, x % y

print(f"GCD of {a} and {b}:", x)
