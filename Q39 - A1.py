# Compute salary with overtime (> 40 hrs at 1.5x rate)
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours <= 40:
    salary = hours * rate
else:
    salary = (40 * rate) + (hours - 40) * (rate * 1.5)

print("Total Salary:", salary)
