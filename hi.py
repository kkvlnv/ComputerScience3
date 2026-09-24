class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}")
        print(f"New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"New balance: {self.__balance}")
        else:
            print("Insufficient balance.")

    def display_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Owner: {self.__owner}")
        print(f"Balance: {self.__balance}")

    def get_account_number(self):
        return self.__account_number


class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance, interest_rate):
        super().__init__(account_number, owner, balance)
        self.__interest_rate = interest_rate

    def add_interest(self):
        # We can't directly access __balance because it is private
        print(f"Interest rate: {self.__interest_rate}%")

    def display_info(self):
        super().display_info()
        print(f"Interest Rate: {self.__interest_rate}%")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, owner, balance, overdraft_limit):
        super().__init__(account_number, owner, balance)
        self.__overdraft_limit = overdraft_limit

    def display_info(self):
        super().display_info()
        print(f"Overdraft Limit: {self.__overdraft_limit}")


# CREATE OBJECTS

account1 = BankAccount("A001", "Ana", 5000)

account2 = SavingsAccount(
    "A002",
    "Mark",
    10000,
    3.5
)

account3 = CheckingAccount(
    "A003",
    "Lia",
    7000,
    2000
)


accounts = [account1, account2, account3]


# USER INTERACTION

search = input("Enter account number to search: ")

found = False

for account in accounts:

    if account.get_account_number() == search:

        found = True

        print("\nAccount found!")
        print("--------------------")

        account.display_info()

        # POLYMORPHISM / RUNTIME TYPE CHECKING

        if isinstance(account, SavingsAccount):
            print("Account Type: Savings Account")

        elif isinstance(account, CheckingAccount):
            print("Account Type: Checking Account")

        else:
            print("Account Type: Bank Account")

        break


if not found:
    print("Account not found.")
