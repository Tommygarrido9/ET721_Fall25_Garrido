class BankAccount(object):
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    # method to add the deposited amount of money into the account
    def deposit(self, amount):
        self.balance += amount
        if(amount < 0):
            return "ERROR! You cannot deposit negative dollars!"
        return self.balance
    # method to subtract the withdrawn amount of money from the account 
    def withdraw(self, amount):
        self.balance -= amount
        if(amount > self.balance):
            return "ERROR! You are overdrawing!"
        elif(amount < 0):
            return "ERROR! You cannot withdraw negative dollars!"
        return self.balance