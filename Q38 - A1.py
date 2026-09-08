# Check if a 3-digit number is an Armstrong number
n = int(input("Enter a 3-digit number: "))

temp = n
d1 = temp % 10
temp //= 10
d2 = temp % 10
temp //= 10
d3 = temp % 10

if (d1**3 + d2**3 + d3**3) == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
