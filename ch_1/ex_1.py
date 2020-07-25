#implement the simple methods getNum and getDen that will return the numerator and denominator of a fraction. 

class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den


if __name__ == '__main__':
    frac = Fraction(2, 3)
    assert 2 == frac.getNum()
    assert 3 == frac.getDen()


