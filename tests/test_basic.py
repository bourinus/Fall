# -*- coding: utf-8 -*-
import unittest
from source.fall import define

class BasicTestSuite(unittest.TestCase):
    """
    Basic test cases.
    """

    def test_define0(self):
        print("define: test", self)
        assert define('0') == '0'

    def test_define1(self):
        print("define: test", self)
        assert define('1') == '1'

    def test_define2(self):
        print("define: test", self)
        assert define('2'), '2'

    def test_defineM1(self):
        print("define: test", self)
        assert define([0, 1, 2]) == [2, 1, 0]

    def test_defineM2(self):
        print("define: test", self)
        assert define([1, 2, 3]) == [3, 2, 1]
    @unittest.expectedFailure
    def test_baddefine(self):
        assert define(["None"]) == ""
# def test_infinite_2loop(self):
#  print("test_infinite_2loop", self)
#  assert (fall.infinite_2loop(24), 26)
# def test_infinite_3loop(self):
#  print("test_infinite_3loop", self)
#  assert (fall.infinite_3loop(23), 27)
# def test_spell(self):
#  print("test_spell", self)
#  assert (fall.spell('1000'), '[ 1,0]')
#  assert (fall.spell( 100), [ 1,0])
#  assert (fall.spell(  10), [ 0,10])
# 
# def test_signature_25(self):
#  print("test_signature_25", self)
#  assert (fall.signature_25('23'), '27')
# def test_signature_15(self):
#  print("test_signature_15", self)
#  assert (fall.signature_15(23), 27)
# def test_signature_5(self):
#  print("test_signature_5", self)
#  assert (fall.signature_5(23), 27)
if __name__ == '__main__':
    unittest.main()
