name = input("Enter your name: ")
number = input("Enter your phone number: ")
bank_id = input("Enter your bank ID: ")

minimum_deposit = int(input("Enter deposit amount: "))
withdraw = int(input("Enter withdraw amount: "))

balance = 0

# Phone number validation
if len(number) == 10 and number.isdigit():
    print("Phone number is valid")
else:
    print("Phone number is not valid")

# Bank ID validation
if len(bank_id) == 12 and bank_id.isdigit():
    print("Bank ID is valid")
else:
    print("Bank ID is not valid")

# Deposit condition
if minimum_deposit >= 500:
    balance = balance + minimum_deposit
    print("Amount added successfully")
else:
    print("Minimum deposit should be 500")

# Withdraw condition
if withdraw <= balance:
    balance = balance - withdraw
    print("Withdraw successful")
else:
    print("Insufficient balance")

print("\n--- Account Details ---")
print("Name:", name)
print("Phone:", number)
print("Bank ID:", bank_id)
print("Current Balance:", balance)
