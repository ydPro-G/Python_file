# 11 测试函数






print("\n11.1.1")
# 11.1.1 单元测试和测试用例

 # 标准库中的模块unittest提供了代码测试工具

 # 单元测试用于核实函数的某个方面没有问题
 # 测试用例是一组单元测试，这些单元测试一起核实函数在各种情况下的行为都符合要求

 # 全覆盖测试包含一整套单元测试





print('\n11.1.2')

 # 可通过测试
  # 导入模块unittest以及要测试的函数
  # 创建一个继承unittest。TestCase的类，编写方法对函数行为不同方面进行测试


# 检查函数get_formatted_name()在给定名和姓时能否正常工作


 # 导入模块unittest
# import unittest
#  # 导入要测试的函数 get_formatted_name()
# from name_function import get_formatted_name

#  # 编写一个类，用于包含针对函数的单元测试，类必须继承unittest.TestCase类
# class NamesTestCase(unittest.TestCase):
#     """测试name_function.py"""

#     def test_first_last_name(self):
#         """能够正确处理像Janis Joplin这样的姓名吗？"""
#         formatted_name = get_formatted_name('janis','joplin')  # 调用要测试的函数，将结果存储到变量中
#         self.assertEqual(formatted_name,'Janis Jopiln') # 断言方法[断言：相等]:调用了断言方法，并向它传递变量与预期要实现的结果，对变量与结果进行比较，如果相等就ok，不相等就报异常

# unittest.main()









print('\n11.1.3')

# 11.1.3 不能通过的测试
 # 会报一个traceback(回溯),指出get_formatted_name有问题,缺少一个必要的位置实参








print('\n11.1.4')
# 11.1.4 测试未通过怎么办

 # 检查刚对函数做出的修改，找出导致函数行为不符合预期的修改








print('\n11.1.5')
# 11.1.5 新测试
 # 用于测试包含中间名的名字
 # 在NamesTestCase类中添加一个新方法

import unittest
 # 导入要测试的函数 get_formatted_name()
from name_function import get_formatted_name

 # 编写一个类，用于包含针对函数的单元测试，类必须继承unittest.TestCase类
class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis','joplin') 
        self.assertEqual(formatted_name,'Janis Joplin') # 断言

 # 方法名必须以test打头，这样才会自动运行
    def test_first_last_middle_name(self):
        """能够正确处理像Wolfgang Amadeus Mozart这样的名字吗？"""
        formatted_name = get_formatted_name('one','two','three')
        self.assertEqual(formatted_name,'One Three Two')  # 断言方法[断言：相等]:调用了断言方法，并向它传递变量与预期要实现的结果，对变量与结果进行比较，如果相等就ok，不相等就报异常

unittest.main()








