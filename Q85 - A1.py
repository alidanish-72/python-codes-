# Hollow rectangle
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

for i in range(rows):
    if i == 0 or i == rows - 1:
        print("* " * cols)
    else:
        print("*" + " " * (2 * cols - 3) + "*")
