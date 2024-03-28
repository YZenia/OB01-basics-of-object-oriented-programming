class BankAccount():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"ВЫ успешно пополнили счёт. Сумма на счете - {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print(f"недостаточно средст на счёте")
        elif money < self.balance:
            self.balance -= money
            print(f"вы успешно сняли {money} рублей. Остаток на счёте: {self.balance}")

    def show_balance(self):
        print(f"Текущий баланс - {self.balance}")

man = BankAccount("21456", 600)

man.show_balance()
man.withdraw(450)
man.withdraw(500)
man.deposit(23000)