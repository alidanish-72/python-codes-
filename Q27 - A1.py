# Calculate electricity bill based on slab rates
units = float(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = 100 * 1.5 + (units - 100) * 2.5
elif units <= 300:
    bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4.0
else:
    bill = 100 * 1.5 + 100 * 2.5 + 100 * 4.0 + (units - 300) * 5.0

print("Total Electricity Bill:", bill)
