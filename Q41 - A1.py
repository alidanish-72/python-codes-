# Clock Angle: Calculate the smaller angle between hour and minute hands
hour = int(input("Enter hour (1-12): "))
minute = int(input("Enter minute (0-59): "))

hour_angle = (hour % 12) * 30 + minute * 0.5
minute_angle = minute * 6

diff = abs(hour_angle - minute_angle)
angle = min(diff, 360 - diff)

print("Smaller angle:", angle, "degrees")
