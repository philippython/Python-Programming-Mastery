transactions = [200, 455.23, -306.5, 25000, -642.21, -133.9, 79.97, 1300, 5000, 3400, -150, -790, -3210, -1000, 8500, -30]


# step 1 : create a variable balance
balance = 0 
# step 2 : Loop through transactions list
for transaction in transactions:
    # step 3 : add positive amount to balance and substract negative amount from balance
    if transaction > 0 : 
        balance += transaction
        print(f"User has been credited ${transaction}")
    else:
        balance -= transaction
        print(f"User has been debited ${transaction}")

# step4 : print message - > User's balance is $4500
print(f"User's total balance is ${balance}")