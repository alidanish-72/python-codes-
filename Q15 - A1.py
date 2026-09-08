# Count the number of set bits in a number
n = int(input("Enter a number: "))

count = 0
temp = abs(n)
while temp > 0:
    count += temp & 1
    temp >>= 1

print("Number of set bits:", count)
