# Using a single recursive function, print numbers in increasing then decreasing order
def print_inc_dec(n, current=1):
    if current > n:
        return
    print(current, end=" ")
    print_inc_dec(n, current + 1)
    print(current, end=" ")

n = int(input("Enter N: "))
print_inc_dec(n)
print()
