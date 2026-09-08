# Given an hour (0-23), print Morning, Afternoon, Evening, or Night
hour = int(input("Enter hour (0-23): "))

if 5 <= hour < 12:
    print("Morning")
elif 12 <= hour < 17:
    print("Afternoon")
elif 17 <= hour < 21:
    print("Evening")
else:
    print("Night")
