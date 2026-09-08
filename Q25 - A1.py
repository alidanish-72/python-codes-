# Given marks (0-100), print grade: A (>=90), B (>=80), C (>=70), D (>=60), F (<60)
marks = float(input("Enter marks (0-100): "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
