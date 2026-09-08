# Check if a number is a palindrome
n = int(input("Enter a number: "))

temp = abs(n)
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if n >= 0 and rev == n:
    print("Palindrome")
else:
    print("Not a palindrome")
