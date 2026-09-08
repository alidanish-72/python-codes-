# Happy Number: Determine whether a number reaches 1 with sum of squared digits
n = int(input("Enter a number: "))

seen = set()
curr = n
while curr != 1 and curr not in seen:
    seen.add(curr)
    curr = sum(int(d) ** 2 for d in str(curr))

if curr == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")
