# Print Fibonacci series up to N terms
n = int(input("Enter number of terms N: "))

a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
