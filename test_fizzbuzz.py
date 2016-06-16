import unittest
import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
	def  test_returns_fizz_when_divisible_by_three(self):
		self.assertEqual(fizzbuzz.fizz_buzz(3),'fizz')

	def  test_returns_fizz_when_divisible_by_five(self):
                self.assertEqual(fizzbuzz.fizz_buzz(5),'buzz')

	def  test_returns_fizz_when_divisible_by_both(self):
                self.assertEqual(fizzbuzz.fizz_buzz(15),'fizz buzz')
