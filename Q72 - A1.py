# Convert binary to decimal
b = input("Enter binary number: ")

decimal = 0
for bit in b:
    decimal = decimal * 2 + int(bit)

print("Decimal:", decimal)
