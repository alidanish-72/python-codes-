# Compute: 1! + 2! + 3! + ... + N!
n = int(input("Enter N: "))

total = 0
fact = 1
for i in range(1, n + 1):
    fact *= i
    total += fact

print("Sum of factorials:", total)
