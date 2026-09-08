# Convert temperature from Celsius to Fahrenheit and vice versa
temp = float(input("Enter temperature: "))
choice = input("Convert to (C/F): ").upper()

if choice == "F":
    print("Fahrenheit:", (temp * 9/5) + 32)
elif choice == "C":
    print("Celsius:", (temp - 32) * 5/9)
else:
    print("Invalid choice")