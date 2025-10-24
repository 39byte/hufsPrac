import random

class BankAccount:
    def __init__(self, name, money = 0):
        self.name = name
        self.acc_num_fr = int(random.random() * 10**6)
        self.acc_num_bk = int(random.random() * 10**4)
        self.money = money

    def deposit(self, amount):
        self.money = self.money + amount

    def withdraw(self, amount):
        self.money = self.money - amount if self.money >= amount else print(f"{self.name}님, 잔액이 부족합니다.")

    def check(self):
        print(f"{self.name}님의 계좌 : {self.acc_num_fr}-{self.acc_num_bk}, 잔액 : {self.money}원")

acc1 = BankAccount("Han Jiwon")
acc1.check()

acc1.deposit(50000)
acc1.withdraw(30000)

acc1.check()

acc2 = BankAccount("Yun Haesol")
acc2.check()
acc2.withdraw(30000)