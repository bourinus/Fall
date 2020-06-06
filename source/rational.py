# coding: utf-8
class RationalException(Exception):
    
    def __init__(self, message):
        Exception.__init__(self, message)


class Rational(object):    

    def __init__(self, num=0, den=1):
        self.numerator = num
        self.denominator = den
        self.simplify()        
    
    @property
    def numerator(self):
        return self.__numerator
     
    @numerator.setter 
    def numerator(self, newNum):
        if isinstance(newNum, int) == False:
            raise RationalException("Numerator must be an integer")
        self.__numerator = newNum
         
    @property
    def denominator(self):
        return self.__denominator
    
    @denominator.setter 
    def denominator(self, newDen):
        if isinstance(newDen, int) == False:
            raise RationalException("Denominator must be an integer")
        if newDen == 0:
            raise RationalException("Denominator cannot be zero")
        self.__denominator = newDen
         
    def simplify(self): 
        if self.__numerator > self.__denominator:
            a = self.__numerator
            b = self.__denominator
        else:
            b = self.__numerator
            a = self.__denominator
        
        while True:
            rest = a % b
            if rest == 0: break
            a = b
            b = rest
        pgcd = b
        self.__numerator //= pgcd  # Division enti�re 
        self.__denominator //= pgcd 
            
    def __str__(self):  
        return "[%d/%d]" % (self.__numerator, self.__denominator)
    
    def __add__(self, r2):
        return Rational(
            self.numerator * r2.denominator + self.denominator * r2.numerator,
            self.denominator * r2.denominator
        )

    # __sub__    __mul__   __truediv__
    
    def __lt__(self, r2):
        return self.numerator * r2.denominator < self.denominator * r2.numerator

    # __le__   __gt__   __ge__   __eq__   __ne__ 
    
    def toFloat(self):
        return self.__numerator / self.__denominator
        
    def __iter__(self):
        self.__iterPos = 0
        return self
    
    def next(self):  # For Python 2.x
        return self.__next__()
    
    def __next__(self):  # For Python 3.x
        self.__iterPos += 1
        if self.__iterPos == 1:
            return self.numerator
        elif self.__iterPos == 2:
            return self.denominator
        else:
            raise StopIteration()
    
