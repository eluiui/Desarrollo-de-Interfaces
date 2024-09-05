class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, deposit):
        self.balance = self.balance + deposit
        print("You've deposited", deposit, "euros into your bank account")
        print("Updated balance:", self.balance)
        
    def withdraw(self, withdrawal):
        if withdrawal > self.balance:
            print("Insufficient balance")
            print("Updated balance:", self.balance)
        else:
            self.balance = self.balance - withdrawal
            print("You've withdrawn", withdrawal, "euros")
            print("Updated balance:", self.balance)
def main():
    bankAccount1 = BankAccount("Paul", 1000000)
    
    print("1. Deposit")
    print("2. Withdraw")
    
    choice = input("Choose an operation: ")
    
    if choice == '1':
        deposit = int(input("Deposit: "))
        bankAccount1.deposit(deposit)
    elif choice == '2':
        withdraw = int(input("Withdraw: "))
        bankAccount1.withdraw(withdraw)
    else:
        print("Sorry we couldn't perform the operation you asked for")
        
if __name__ == "__main__":
    main()