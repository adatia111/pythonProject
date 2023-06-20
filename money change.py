bill = int(input("enter your bill"))
paid = int(input("enter amount paid"))
balance = paid - bill
print("............................")
print("the balance is",balance)

if balance=>50:
    n50 = int(balance/50)
    print("50 pound notes",n50)
    balance = balance - (n50*50)
