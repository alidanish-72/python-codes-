# Find LCM of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b
while y != 0:
    x, y = y, x % y
gcd = x

lcm = (a * b) // gcd
print(f"LCM of {a} and {b}:", lcm)
