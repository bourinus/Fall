# -*- coding: utf-8 -*-

from .context import tests
import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(fall.define())


if __name__ == '__main__':
    unittest.main()
