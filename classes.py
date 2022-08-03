class BankAccount:
    instances = [] # This will store every single instance of a BankAccount
    account_numbers = [0] # This will store all the BankAccount numbers seperately, to make it simple to search. 

    def __init__(self, balance, int_rate):
        # Basic Attributes
        self.account_number = max(BankAccount.account_numbers) + 1
        self.balance = balance
        self.int_rate = int_rate

        # Append new instances to the list.
        BankAccount.instances.append(self)
        BankAccount.account_numbers.append(self.account_number)
    
    # This Method will either turn a specific account, or all current accounts
    @classmethod
    def audit_accounts(cls, account_number = 0):
        if account_number == 0:
                return cls.instances
        else: 
            for account in cls.instances:
                if account.account_number == account_number:
                    return account

    # Account Query Method
    def account_query(self):
        return [self.account_number, self.balance, self.int_rate]

    # Deposit Method with some simple checks.
    def deposit(self, amount):
        if amount <= 0:
            return 'Invalid deposit amount'
        else:
            self.balance += amount
        return self

    # Withdraw Method with some simple checks.
    def withdraw(self, amount):
        if amount > self.balance:
            difference = amount - self.balance
            self.balance -= amount
            return f'Overdraft Warning - Account Overdrafted By: {difference}'
        elif amount <= 0:
            return 'Invalid withdraw amount'
        else:
            self.balance -= amount
        return self

    # Interest Method that increases balance based on account's interest rate.
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


class User:
    # Constructors
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = [BankAccount(0, 0.02)]

    def get_user_data(self, acc_index  = 0):
        return [self.name, self.email, self.account[acc_index].account_query()]

    def make_deposit(self, amount, acc_index = 0):
        self.account[acc_index].deposit(amount)

    def make_withdraw(self, amount, acc_index  = 0):
        self.account[acc_index].withdraw(amount)

    def display_user_balance(self, acc_index  = 0):
        print(self.account[acc_index].balance)

    def transfer_balance(self, amount, other_user, other_user_acc_index = 0, acc_index = 0):
        if other_user.account[other_user_acc_index].account_number != 0:
            self.make_withdraw(amount, acc_index)
            other_user.make_deposit(amount, other_user_acc_index)
        else:
            return 'Invalid Account'


testUser = User("Robert Teets", "teetsrobert@gmail.com")
secondUser = User("Amelia Troy", "atroy97@gmail.com")
testUser.make_deposit(100)
testUser.make_withdraw(50)

testUser.display_user_balance(0)
secondUser.display_user_balance(0)

testUser.transfer_balance(50, secondUser, 0, 0)

testUser.display_user_balance(0)
secondUser.display_user_balance(0)