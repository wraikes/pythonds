def gcd(m, n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    
    return n


class Fraction:
    def __init__(self,top,bottom):
        self.common = gcd(top, bottom)
        self.num = top // self.common
        self.den = bottom // self.common

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self,otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum
    

if __name__=='__main__':
    frac_1 = Fraction(2, 5)
    frac_2 = Fraction(6, 10)
    frac_3 = frac_1 + frac_2
    assert frac_3.num == 1
    assert frac_3.den == 1 

