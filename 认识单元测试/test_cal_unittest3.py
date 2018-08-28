from calculator import Count
import unittest

class MyTest(unittest.TestCase):  #将多次用到的setUp()和tearDown()封装成类
	
	def setUp(self):
		print('test case start')

	def tearDown(self):
		print('test case end')
		
class TestAdd(MyTest):  #加法
	
	def test_add(self):
		j = Count(2, 3)
		self.assertEqual(j.add(), 5)

	def test_add2(self):
		j = Count(41, 76)
		self.assertEqual(j.add(), 117)

class TestSub(MyTest):   # 减法
	
	def test_sub(self):
		j = Count(2, 3)
		self.assertEqual(j.sub(), -1)

	def test_sub2(self):
		j = Count(76, 41)
		self.assertEqual(j.sub(), 35)
		
if __name__ == '__main__':
	unittest.main()	