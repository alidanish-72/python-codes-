# Find x^n (power) without using built-in pow function
x = float(input("Enter base x: "))
n = int(input("Enter exponent n: "))

res = 1.0
for _ in range(abs(n)):
    res *= x

if n < 0:
    res = 1 / res

print(f"{x}^{n} =", res)
