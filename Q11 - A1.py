# Check if a number is even or odd using bitwise AND (n & 1)
n = int(input("Enter a number: "))

if n & 1 == 0:
    print("Even")
else:
    print("Odd")
