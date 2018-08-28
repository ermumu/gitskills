import unittest

'''/////////// 第一种调用测试用例方法 ////////// '''       
# # 加载测试文件
# import TTest_add
# import TTest_sub

# # 构造测试集
# suite = unittest.TestSuite()

# suite.addTest(TTest_add.TestAdd('test_add'))
# suite.addTest(TTest_add.TestAdd('test_add2'))

# suite.addTest(TTest_sub.TestSub('test_sub'))
# suite.addTest(TTest_sub.TestSub('test_sub2'))

# if __name__ == '__main__':
# 	runner = unittest.TextTestRunner()
# 	runner.run(suite)



'''/////////// 第二种调用测试用例方法 ////////// '''     
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern = 'TTest*.py')

if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	runner.run(discover)