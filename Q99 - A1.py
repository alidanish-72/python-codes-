# Alphabet triangle (sequential)
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
