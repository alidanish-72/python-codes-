# Find the sum of a series: x - x^3/3! + x^5/5! - x^7/7! ... (sin series)
import math

x = float(input("Enter angle in radians x: "))
terms = int(input("Enter number of terms: "))

total = 0.0
sign = 1
for i in range(terms):
    power = 2 * i + 1
    term = (x ** power) / math.factorial(power)
    total += sign * term
    sign = -sign

print("Sum of series:", total)
