#!/usr/bin/python
import unittest
from task6 import *

from unittest import TestCase


class TestPrime(TestCase):

    def test_is_prime(self):
        """Test for is _prime"""
        c1 = Myclass()
        self.assertFalse(c1.write_json())

if __name__ == '__main__':
    unittest.main()
