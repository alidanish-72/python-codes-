# Check if the Kth bit of a number is set or not
n = int(input("Enter a number: "))
k = int(input("Enter bit position K (0-indexed): "))

if (n & (1 << k)) != 0:
    print(f"Bit {k} is SET")
else:
    print(f"Bit {k} is NOT SET")
