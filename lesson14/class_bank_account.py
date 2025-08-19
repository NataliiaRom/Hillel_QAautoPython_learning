class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

account = BankAccount('DA234565',456000)
print(account.get_account_number())
print(account.get_balance())

account.set_account_number('UA43634735')
account.set_balance(46540000)

print(account.get_account_number())
print(account.get_balance())
