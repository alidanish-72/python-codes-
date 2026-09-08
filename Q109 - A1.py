# X pattern
n = int(input("Enter odd size (e.g. 5): "))

for i in range(n):
    for j in range(n):
        if j == i or j == n - 1 - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
