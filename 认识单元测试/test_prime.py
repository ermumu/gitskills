from count_prime import is_prime
import unittest

class Test(unittest.TestCase):
	def setUp(self):
		print("test is_prime start")

	def test_case(self):
		self.assertTrue(is_prime(11), msg = "is not prime !")

	def tearDown(self):
		print("test is_prime end")

if __name__ == '__main__':
	unittest.main()