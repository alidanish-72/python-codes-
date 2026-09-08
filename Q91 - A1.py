# 1-0 alternating triangle
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print((1 - j % 2), end=" ")
    print()
