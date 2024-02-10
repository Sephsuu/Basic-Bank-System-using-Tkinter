class BankAccount:
    def __init__(self, account_number, account_name, balance):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def get_balance(self):
        return "{:.2f}".format(self.balance)
class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_name, balance):
        super().__init__(account_number, account_name, balance)

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_name, balance):
        super().__init__(account_number, account_name, balance)

accounts = {
    "0000": CheckingAccount("202305490", "Rome Jay", 1_000),
    "2024": CheckingAccount("202207364", "Ramon Batumbakal", 500_000),
    "0930": CheckingAccount("202193763", "Lola Flora", 200_000),
    "6118": CheckingAccount("202391744", "Antonio Pigafetta", 10_000),
    "3783": CheckingAccount("202312133", "Andres Aguinaldo", 15_000),
}

savings_accounts = {
    "0000": SavingsAccount("202305490", "Rome Jay", 10_000),
    "2024": SavingsAccount("202207364", "Ramon Batumbakal", 100_000),
    "0930": SavingsAccount("202193763", "Lola Flora", 75_000),
    "6118": SavingsAccount("202391744", "Antonio Pigafetta", 25_000),
    "3783": SavingsAccount("202312133", "Andres Aguinaldo", 25_000),
}