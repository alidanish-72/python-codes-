# Hollow right-angled triangle
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    if i == 1:
        print("*")
    elif i == n:
        print("*" * n)
    else:
        print("*" + " " * (i - 2) + "*")
