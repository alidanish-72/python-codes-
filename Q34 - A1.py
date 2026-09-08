# Find the roots of a quadratic equation (ax^2 + bx + c = 0)
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d = b**2 - 4 * a * c

if d > 0:
    r1 = (-b + d**0.5) / (2 * a)
    r2 = (-b - d**0.5) / (2 * a)
    print("Real and distinct roots:", r1, "and", r2)
elif d == 0:
    r = -b / (2 * a)
    print("Real and equal roots:", r)
else:
    real_part = -b / (2 * a)
    imag_part = (-d)**0.5 / (2 * a)
    print(f"Imaginary roots: {real_part} + {imag_part}i and {real_part} - {imag_part}i")
