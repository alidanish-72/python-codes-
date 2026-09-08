# Read cost price and selling price - print profit, loss, or no profit no loss
cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    print("Profit:", sp - cp)
elif cp > sp:
    print("Loss:", cp - sp)
else:
    print("No Profit No Loss")
