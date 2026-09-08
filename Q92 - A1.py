# Pascal's triangle
import math

n = int(input("Enter number of rows: "))

for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(i + 1):
        print(math.comb(i, j), end=" ")
    print()
