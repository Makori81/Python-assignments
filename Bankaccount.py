class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        return self.balance

    def customer_details(self):
        return (f"Customer Name: {self.customer_name}\n"
                f"Account Number: {self.account_number}\n"
                f"Date of Opening: {self.date_of_opening}\n"
                f"Balance: {self.balance}")

def main():
    # Input bank details
    account_number = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))
    date_of_opening = input("Enter date of opening (YYYY-MM-DD): ")
    customer_name = input("Enter customer name: ")

    # Create BankAccount instance
    account = BankAccount(account_number, balance, date_of_opening, customer_name)

    while True:
        print("\nChoose an action:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Customer Details")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            print(f"Amount deposited: {account.deposit(amount)}")
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            result = account.withdraw(amount)
            print(result)
        elif choice == '3':
            print(f"Current Balance: {account.check_balance()}")
        elif choice == '4':
            print(account.customer_details())
        elif choice == '5':
            print("Exiting")
            break
        else:
            print("Invalid choice. Please try again.")

    main()
