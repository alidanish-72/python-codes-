# Check if a number is positive, negative, or zero - then if positive check even/odd
num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
elif num < 0:
    print("Negative")
else:
    print("Zero")
