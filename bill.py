total = float(input("Enter total bill amount: "))
paid = float(input("Enter amount paid: "))

due = total - paid

if due > 0:
    print("Customer still owes:", due)
elif due < 0:
    print("Return change:", -due)
else:
    print("Payment complete. No due or change.")
