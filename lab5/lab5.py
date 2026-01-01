class BankAccount:
    def __init__(self,pin):
        self.pin=pin
        self.balance=0
    
    def deposit(self,pin,amount):
        if self.pin==pin:
            self.balance = self.balance+amount
            print(f'таны данс {amount}Т р цэнэглэгдэж нийт үлдэгдэл {self.balance}T боллоо.')
        else:
            print('таны пин код буруу байна')


    def withdraw(self,pin,amount):
        if self.pin==pin:
            self.balance = self.balance-amount
            print(f'таны данс {amount}Т р хасагдаж нийт үлдэгдэл {self.balance}T боллоо.')
        else:
            print('таны пин код буруу байна')

    def get_balance(self,pin):
        if self.pin == pin:
            print(f'таны дансны үлдэгдэл{self.balance}T')
        else:
            print('Таны пин код буруу байна!')
            
    user = BankAccount('pin')
    user.deposit('pin',15499)
    user.withdraw('pin',499)
    user.get_balance('pin')