# Ticket Pricing: Calculate ticket price based on customer age
age = int(input("Enter age: "))

if age < 5:
    price = 0
elif age <= 12:
    price = 10
elif age <= 60:
    price = 20
else:
    price = 15

print("Ticket Price:", price)
