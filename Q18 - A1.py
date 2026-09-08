# Find the largest of two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("Largest:", a)
elif b > a:
    print("Largest:", b)
else:
    print("Both numbers are equal")
