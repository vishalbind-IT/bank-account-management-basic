class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ₹{amount}. Remaining Balance: ₹{self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")


def main():
    name = input("Enter account holder name: ")
    account = BankAccount(name)

    while True:
        print("\n===== Bank Menu =====")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        try:
            choice = int(input("Enter choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            try:
                amt = float(input("Enter amount to deposit: "))
                account.deposit(amt)
            except ValueError:
                print("Enter a valid number.")
        elif choice == 2:
            try:
                amt = float(input("Enter amount to withdraw: "))
                account.withdraw(amt)
            except ValueError:
                print("Enter a valid number.")
        elif choice == 3:
            account.check_balance()
        elif choice == 4:
            print("Thank you for using the bank system!")
            break
        else:
            print("Invalid choice. Please select from 1-4.")


if __name__ == "__main__":
    main()
