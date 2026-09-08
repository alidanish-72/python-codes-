# Scholarship Eligibility: Based on marks, attendance, and family income
marks = float(input("Enter marks percentage: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter annual family income: "))

if marks >= 80 and attendance >= 75 and income <= 250000:
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")
