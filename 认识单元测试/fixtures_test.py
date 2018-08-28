import unittest

# setUpModule/tearDownModule 在整个模块开始与结束时被执行
def setUpModule():
	print('test module start >>>>>>>>>>')
def tearDownModule():
	print('test module end >>>>>>>>>>')

class MyTest(unittest.TestCase):
	
	# setUpClass/tearDownClass 在测试类的开始与结束时被执行，需要通过@classmethod装饰
	@classmethod
	def setUpClass(cls):
		print('test class start ==========>')
	
	@classmethod
	def tearDownClass(cls):
		print('test class end ==========>')

	
	# setUp/tearDown 在测试用例开始与结束时被执行
	def setUp(self):
		print('test case start -->')

	def tearDown(self):
		print('test case end -->')

	
	def test_case1(self):
		print('test_case1')

	def test_case2(self):
		print('test_case2')

if __name__ == '__main__':
	unittest.main()