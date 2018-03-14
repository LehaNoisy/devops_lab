#!/usr/bin/python

import unittest
from task6 import Myclass
from unittest import TestCase


class TestPrime(TestCase):

    def test_is_prime(self):
        """Test for clearis _prime"""
        c1 = Myclass()
        self.assertFalse(c1.write_json())


if __name__ == '__main__':
    unittest.main()
