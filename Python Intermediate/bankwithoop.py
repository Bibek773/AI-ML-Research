class Account:
    def __init__(self, bal, acc, name):
        self.name = name
        self.balance = bal
        self.account = acc
    
    def debit(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print(f"Rs {amt} is debited from your account")
            print(f"Your new balance is Rs {self.balance}")
        else:
            print("Insufficient balance! Transaction failed.")
            print(f"Your current balance is Rs {self.balance}")
    
    def credit(self, amt):
        self.balance += amt
        print(f"Your account has been credited with Rs {amt}.")
        print(f"Your new balance is Rs {self.balance}")
    
    def getinfo(self):
        print("\nAccount Holder's Name:", self.name)
        print("Account Number:", self.account)
        print("Account Balance: Rs", self.balance)


accounts = {}
current_account = None

print("\nWELCOME TO BANK MANAGEMENT SYSTEM\n")

while True:
    print("\nSelect:")
    print("1. Get Account Info")
    print("2. Credit")
    print("3. Debit")
    print("4. Add New Account")
    print("5. Switch Account")
    print("6. Exit")
    
    choice = input("\nSelect an option (1-6): ")
    
    if choice == '1':
        if current_account is None:
            print("\nNo account selected! Please create an account first.")
        else:
            current_account.getinfo()
    
    elif choice == '2':
        if current_account is None:
            print("\nNo account selected! Please create an account first.")
        else:
            amt = float(input("Enter amount to credit: Rs "))
            current_account.credit(amt)
    
    elif choice == '3':
        if current_account is None:
            print("\nNo account selected! Please create an account first.")
        else:
            amt = float(input("Enter amount to debit: Rs "))
            current_account.debit(amt)
    
    elif choice == '4':
        print("\n--- CREATE NEW ACCOUNT ---")
        name = input("Enter account holder's name: ")
        acc_num = int(input("Enter account number: "))
        initial_bal = float(input("Enter initial balance: Rs "))
        
        new_account = Account(initial_bal, acc_num, name)
        accounts[acc_num] = new_account
        current_account = new_account
        print(f"\nAccount created successfully for {name}!")
    
    elif choice == '5':
        if len(accounts) == 0:
            print("\nNo accounts available! Please create an account first.")
        else:
            print("\n--- AVAILABLE ACCOUNTS ---")
            for acc_num, account in accounts.items():
                print(f"Account Number: {acc_num} | Name: {account.name}")
            
            acc_num = int(input("\nEnter account number to switch: "))
            current_account = accounts[acc_num]
            print(f"\nSwitched to account of {current_account.name}")
    
    elif choice == '6':
        print("\nThank you for using Bank Management System!")
        break
    
    else:
        print("\nInvalid choice! Please select 1-6.")