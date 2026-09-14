class Account:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Rs.{amount} deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Rs.{amount} withdrawn successfully.")

    def get_balance(self):
        return self.__balance

    def show_details(self):
        print("\nAccount Number:", self.account_no)
        print("Name:", self.name)
        print("Balance:", self.__balance)


class SavingsAccount(Account):
    def __init__(self, account_no, name, balance, interest_rate):
        super().__init__(account_no, name, balance)
        self.interest_rate = interest_rate

    def show_details(self):
        super().show_details()
        print("Account Type: Savings")
        print("Interest Rate:", self.interest_rate, "%")


class CurrentAccount(Account):
    def __init__(self, account_no, name, balance, overdraft_limit):
        super().__init__(account_no, name, balance)
        self.overdraft_limit = overdraft_limit

    def show_details(self):
        super().show_details()
        print("Account Type: Current")
        print("Overdraft Limit:", self.overdraft_limit)


# Objects

account1 = SavingsAccount(
    1001,
    "Ali",
    50000,
    7
)

account2 = CurrentAccount(
    1002,
    "Ahmed",
    80000,
    20000
)

account1.deposit(10000)
account1.withdraw(5000)

account1.show_details()

print("\n-------------------")

account2.withdraw(10000)
account2.show_details()