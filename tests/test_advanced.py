# -*- coding: utf-8 -*-

import unittest

from .context import tests


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(fall.define())


if __name__ == '__main__':
    unittest.main()
