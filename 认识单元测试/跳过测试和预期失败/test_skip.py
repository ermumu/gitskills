import unittest

class MyTest(unittest.TestCase):

	def setUp(self):
		pass

	@unittest.skip('跳过测试')
	def test_skip(self):
		print('test_skip')

	@unittest.skipIf(3 > 2, "当条件为true，跳过测试")
	def test_skipIf(self):
		print('test_skipIf')

	@unittest.skipUnless(3 > 2, "当条件为true，执行测试")
	def test_skipUnless(self):
		print('test_skipUnless')

	@unittest.expectedFailure
	def test_expected_Failure(self):
		assertEquals(2, 3)

	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main()

	# suite = unittest.TestSuite()
	# suite.addTest(MyTest('test_skip'))
	# suite.addTest(MyTest('test_skipIf'))
	# suite.addTest(MyTest('test_skipUnless'))

	# runner = unittest.TextTestRunner()
	# runner.run(suite)
