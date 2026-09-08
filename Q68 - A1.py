# Find the largest and smallest digit in a number
n = abs(int(input("Enter a number: ")))

digits = [int(d) for d in str(n)]
print("Largest digit:", max(digits))
print("Smallest digit:", min(digits))
