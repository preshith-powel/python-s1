class BankAccount:
    def __init__(self, account_number, account_holder_name, account_type, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type=account_type
        self.balance=balance
    
    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self.balance=self.balance+amount
        print("Deposit successful. Your new balance is: ", self.balance)

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance=self.balance-amount
            print("Withdrawal successful. Your new balance is: ", self.balance)
    def getAccntDetails(self):
        return self.account_number, self.account_holder_name, self.account_type, self.balance

if __name__=="__main__":
    accnt_num=input("Enter the account number: ")
    accnt_name=input("Enter the account holder name: ")
    accnt_type=input("Enter the account type: ")
    account = BankAccount(accnt_num,accnt_name,accnt_type)
    while True:
        print("What operation do you want to perform:")
        choice=int(input("Enter 1 if you want to deposit.\nEnter 2 if you want to withdaw.\nEnter 3 to view your account details.\nEnter 4 to quit.\n"))
        if choice == 1:
            account.deposit()
        elif choice == 2:
            account.withdraw()
        elif choice == 3:
            print("Your Account number is: ", account.getAccntDetails()[0])
            print("Your Account holder name is: ", account.getAccntDetails()[1])
            print("Your Account type is: ", account.getAccntDetails()[2])
            print("Your Account balance is: ", account.getAccntDetails()[3])
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please choose a valid option.")
