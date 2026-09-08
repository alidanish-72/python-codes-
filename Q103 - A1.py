# Butterfly pattern
n = int(input("Enter half rows (e.g. 4): "))

for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
