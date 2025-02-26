class BankAccount:
    def __init__(self, name, balance):
        self.account_holder = name
        self.balance = balance

        self.display_balance()
    
    def deposit(self, amout):
        self.balance += amout
        self.display_balance()

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print(f"Action impossible, vous n'avez que {self.balance}€ en banque")

        else:
            self.balance -= amount
            self.display_balance()
        
    def display_balance(self):
        print(f"balance de {self.account_holder} : {self.balance}€")

bank_account = BankAccount("Charles", 50)

print(f"\nJe dépose 10€")
bank_account.deposit(10)

print(f"\nJe retire 100€")
bank_account.withdraw(100)

print(f"\nJe retire 30€")
bank_account.withdraw(30)