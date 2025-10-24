import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.son = numerator
        self.mom = denominator

    def Print(self):
        return f"{self.son} / {self.mom}"\
        
    def Add(self, other):
        same_mom = self.mom * other.mom
        rst_frac_son = self.son * other.mom + other.son * self.mom
        return Fraction(rst_frac_son, same_mom)
    
    def Subtract(self, other):
        same_mom = self.mom * other.mom
        rst_frac_son = self.son * other.mom - other.son * self.mom
        return Fraction(rst_frac_son, same_mom)
    
    def Multiply(self, other):
        mom = self.mom * other.mom
        son = self.son * other.son
        return Fraction(son, mom)
    
    def Divide(self, other):
        mom = self.mom * other.son
        son = self.son * other.mom
        return Fraction(son, mom)
    
class Frac_Cal():
    def __init__(self, son, mom):
        gcd = math.gcd(son, mom)
        self.son = son // gcd
        self.mom = mom // gcd
        return Fraction(self.son, self,mom)


frac1 = Fraction(2, 3)
print(frac1.Print())

frac2 = Fraction(1, 2)
print(frac2.Print())

print("Additon :", frac1.Add(frac2).Print())
print("Subtraction :", frac1.Subtract(frac2).Print())
print("Multiplication :", frac1.Multiply(frac2).Print())
print("Division :", frac1.Divide(frac2).Print())