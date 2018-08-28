from calculator import Count
import unittest

class TestAdd(unittest.TestCase):  #加法
	
	def setUp(self):
		print('test add start')

	def test_add(self):
		j = Count(2, 3)
		self.assertEqual(j.add(), 5)

	def test_add2(self):
		j = Count(41, 76)
		self.assertEqual(j.add(), 117)

	def tearDown(self):
		print('test add end')

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
	# 构造测试集
	suite = unittest.TestSuite()
	suite.addTest(TestAdd('test_add'))
	suite.addTest(TestAdd('test_add2'))
	suite.addTest(TestSub('test_sub'))
	suite.addTest(TestSub('test_sub2'))
	# 执行测试
	runner = unittest.TextTestRunner()
	runner.run(suite)	