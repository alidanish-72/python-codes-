# ATM Withdrawal: Approve or reject withdrawal based on balance and minimum balance
balance = float(input("Enter current balance: "))
amount = float(input("Enter withdrawal amount: "))
min_balance = 500.0

if amount <= 0:
    print("Invalid amount")
elif balance - amount >= min_balance:
    balance -= amount
    print("Withdrawal approved. Remaining balance:", balance)
else:
    print("Withdrawal rejected: Insufficient funds or violates minimum balance of", min_balance)
