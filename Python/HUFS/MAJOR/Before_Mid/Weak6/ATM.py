import random

class BankAccount:
    def __init__(self, name, balance = 0):
        self.owner = name
        self.num1 = int(random.random() * 10**6)
        self.num2 = int(random.random() * 10**6)
        self.money = balance
    
    def deposit(self, amount):
        
        self.money += amount
    
    def Withdraw(self, amount):
        self.money -= amount if self.money >= amount else print("잔액이 부족합니다.")

    def check(self):
        print(f"{self.owner}님의 계좌 : {self.num1}-{self.num2}, 잔액 : {self.money}")

    
account1 = BankAccount("Challie")
account1.check()
account1.deposit(1100)
account1.Withdraw(1000)
account1.check()
