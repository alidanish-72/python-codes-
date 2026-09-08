# Print all prime numbers from 1 to N
n = int(input("Enter N: "))

print(f"Prime numbers up to {n}:")
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()
