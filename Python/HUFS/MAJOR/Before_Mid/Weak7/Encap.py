class Bank_Acc:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = 0
        self.balance = balance  # setter

    @property   # getter
    def balance(self):
        return self._balance
    
    @balance.setter # setter
    def balance(self, value):
        self._balance = float(value)

acc1 = Bank_Acc("Jiwon", 10_000)

print(f"{acc1.owner}'s balance : {acc1.balance}")   # getter