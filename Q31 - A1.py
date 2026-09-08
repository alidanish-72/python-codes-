# Read month number (1-12) and print number of days in that month
month = int(input("Enter month number (1-12): "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif month == 2:
    print("28 or 29 days (leap year)")
else:
    print("Invalid month number")
