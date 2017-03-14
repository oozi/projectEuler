import unittest
from problem12lib import *


class GetPrimesTest(unittest.TestCase):
    def test_input(self):
        self.assertRaises(ValueError, get_primes, -1)
        self.assertRaises(TypeError, get_primes, 9.6)

    def test_one(self):
        self.assertEqual(get_primes(1), [])

    def test_primes(self):
        self.assertEqual(get_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])


class GetDivisorTest(unittest.TestCase):
    def test_input(self):
        self.assertRaises(ValueError, get_divisors, -1)
        self.assertRaises(ValueError, get_divisors, 0)
        self.assertRaises(TypeError, get_divisors, 9.6)

    def test_one(self):
        self.assertEqual(get_divisors(1), [1])

    def test_divisors(self):
        self.assertEqual(get_divisors(200), [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 200])


if __name__ == '__main__':
    unittest.main()
