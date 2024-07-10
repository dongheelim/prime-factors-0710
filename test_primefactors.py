from unittest import TestCase

from primefactors import PrimeFactors


class TestPrimeFactors(TestCase):
    def test_prime_factor_of_1(self):
        self.assertEqual([], self.prime_factor.of(1))
    def test_prime_factor_of_2(self):
        self.assertEqual([2], self.prime_factor.of(2))
    def test_prime_factor_of_3(self):
        self.assertEqual([3], self.prime_factor.of(3))

    def setUp(self):
        super().setUp()
        self.prime_factor = PrimeFactors()