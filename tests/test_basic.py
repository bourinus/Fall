# -*- coding: utf-8 -*-

import unittest

from .context import fall


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

  def test_define(self):
    print("define: test", self)
    self.assertEqual(fall.define('0'), '0')
    self.assertEqual(fall.define('1'), '1')
    self.assertEqual(fall.define('2'), '2')
    self.assertEqual(fall.define([0, 1, 2]), [2, 1, 0])
    self.assertEqual(fall.define([1, 2, 3]), [3, 2, 1])
    self.assertEqual(fall.define([1, 2, 3]), [3, 2, 1])

  # def test_infinite_2loop(self):
  #  print("test_infinite_2loop", self)
  #  self.assertEqual(fall.infinite_2loop(24), 26)
  # def test_infinite_3loop(self):
  #  print("test_infinite_3loop", self)
  #  self.assertEqual(fall.infinite_3loop(23), 27)
  # def test_spell(self):
  #  print("test_spell", self)
  #  self.assertEqual(fall.spell('1000'), '[ 1,0]')
  #  self.assertEqual(fall.spell( 100), [ 1,0])
  #  self.assertEqual(fall.spell(  10), [ 0,10])

  # def test_signature_25(self):
  #  print("test_signature_25", self)
  #  self.assertEqual(fall.signature_25('23'), '27')
  # def test_signature_15(self):
  #  print("test_signature_15", self)
  #  self.assertEqual(fall.signature_15(23), 27)
  # def test_signature_5(self):
  #  print("test_signature_5", self)
  #  self.assertEqual(fall.signature_5(23), 27)


if __name__ == '__main__':
    unittest.main()
