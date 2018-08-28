from calculator import Count
import unittest

class TestSub(unittest.TestCase):   # 减法
	
	def setUp(self):
		print("test sub start")

	def test_sub(self):
		j = Count(2, 3)
		self.assertEqual(j.sub(), -1)

	def test_sub2(self):
		j = Count(76, 41)
		self.assertEqual(j.sub(), 35)

	def tearDown(self):
		print("test sub end")

if __name__ == '__main__':
	unittest.main()