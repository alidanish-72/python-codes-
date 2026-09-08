# Find the product of all digits of a number using recursion
def product_of_digits(n):
    if n < 10:
        return n
    return (n % 10) * product_of_digits(n // 10)

num = abs(int(input("Enter a number: ")))
print("Product of digits:", product_of_digits(num))
