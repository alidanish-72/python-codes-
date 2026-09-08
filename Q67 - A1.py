# Check if a number is an Armstrong number (generalized for any number of digits)
n = int(input("Enter a number: "))

s = str(abs(n))
power = len(s)
total = sum(int(digit) ** power for digit in s)

if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
