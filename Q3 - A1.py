# Calculate simple interest given P, R, T: (P * R * T) / 100
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100

print("Simple Interest:", si)