# Hollow diamond inside rectangle
n = int(input("Enter half size (e.g. 4): "))

for i in range(n):
    print("*" * (n - i) + " " * (2 * i) + "*" * (n - i))

for i in range(n - 1, -1, -1):
    print("*" * (n - i) + " " * (2 * i) + "*" * (n - i))
