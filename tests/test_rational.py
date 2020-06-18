import unittest
from source.rational import Rational

class Test(unittest.TestCase):


    def testSimplify(self):
        r1 = Rational( 2*3*5*7*11, 3*5*7*13 )
        assert r1.numerator == 22
        assert r1.denominator == 13

    def testAddition(self):
        r1 = Rational(1,3)
        r2 = Rational(2,1)
        result = r1 + r2
        assert result.numerator == 7
        assert result.denominator == 3

    def testIterator(self):
        r1 = Rational(1,3)
        r1.__iter__()
        assert r1.__next__() == 1
        assert r1.__next__() == 3
        # Normalement on utilise l'itérateur ainsi : 
        # >>> for value in r1: print(value) 

    @unittest.expectedFailure
    def testBadDenominator(self):
        Rational( 1, 0 )
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
