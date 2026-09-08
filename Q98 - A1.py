# Alphabet triangle (row repeat)
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    char = chr(65 + i - 1)
    print((char + " ") * i)
