import unittest
from employee import Employee  # 文件.类


class testEmployee(unittest.TestCase):
    """测试年薪增长"""
    def setUp(self):
        """创建一个雇员实例"""
        self.staff = Employee('a','b')  # 雇员实例

    def test_give_default_raise(self):
        """测试默认增加"""
        total = self.staff.give_raise()
        self.assertEqual(total,5000)
    
    def test_give_custom_raise(self):
        """测试自定义增加"""
        total = self.staff.give_raise(1000)
        self.assertEqual(total,1000)

unittest.main()
    
    



