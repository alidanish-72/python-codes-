# Check if a valid triangle can be formed given 3 sides
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Valid triangle")
else:
    print("Cannot form a valid triangle")
