def gcd(m, n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    
    return n


class Fraction:
    def __init__(self,top,bottom):
        try:
            self.common = gcd(top, bottom)
            self.num = top // self.common
            self.den = bottom // self.common
        except:
            print('Please input integer')
        
        if self.den < 0:
            self.den *= -1
            self.num *= -1

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __repr__(self):
        return ('Fraction({}, {})').format(self.num, self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self,otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __radd__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __iadd__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)


    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum
    
    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        return Fraction(newnum, newden)

    def __gt__(self, otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = otherfraction.num * self.den

        return firstnum > secondnum

    def __ge__(self, otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = otherfraction.num * self.den

        return firstnum >= secondnum

    def __lt__(self, otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = otherfraction.num * self.den

        return firstnum < secondnum

    def __le__(self, otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = otherfraction.num * self.den

        return firstnum <= secondnum


if __name__=='__main__':
    frac1 = Fraction(2, -3)
    frac2 = Fraction(-3, -5)
    frac1 += frac2

    assert frac1 == Fraction(-1, 15)
    






