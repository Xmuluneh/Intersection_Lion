class Intersection:
    def __init__(self, a=0.0, b=0.0, c=0.0, d=0.0, e=0.0, f=0.0):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getD(self):
        return self.__d

    def getE(self):
        return self.__e

    def getF(self):
        return self.__f

    def isSolvable(self):
        number = (self.__a * self.__b) - (self.__c * self.__d)
        if number != 0:
            return True
        else:
            return False

    def getX(self):
        if self.isSolvable():
            return (self.__e * self.__d - self.__b * self.__f) // (self.__a * self.__b - self.__c * self.__d)
        else:
            "The equation is not solved "

    def getY(self):
        if self.isSolvable():
            return (self.__a * self.__f - self.__c * self.__e) // (self.__a * self.__b - self.__c * self.__d)
        else:
            "The equation is not solved"
