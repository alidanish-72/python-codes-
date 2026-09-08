# Given coordinates (x, y), determine which quadrant the point lies in
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("First Quadrant")
elif x < 0 and y > 0:
    print("Second Quadrant")
elif x < 0 and y < 0:
    print("Third Quadrant")
elif x > 0 and y < 0:
    print("Fourth Quadrant")
elif x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("On Y-axis")
else:
    print("On X-axis")
