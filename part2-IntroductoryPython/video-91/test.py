class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Your balance is: ", self.__balance)
        else:
            print("The value must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Your balance is: ", self.__balance)
        else:
            print("Invalid withdrawal amount or insufficient balance")

account_01 = BankAccount(1000)

# print(account_01.__balance)
account_01.deposit(600)
account_01.withdraw(2300)

# ====================================================
class Account:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
