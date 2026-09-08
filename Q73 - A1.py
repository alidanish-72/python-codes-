# Read numbers until user enters -1, print count and average
total = 0
count = 0

while True:
    num = float(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    total += num
    count += 1

if count > 0:
    print("Count:", count)
    print("Average:", total / count)
else:
    print("No numbers were entered.")
