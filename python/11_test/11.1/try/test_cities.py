import unittest
from city_functions import country


# 测试country函数

class CountryTeseCase(unittest.TestCase):
    """测试country函数"""

    def test_country(self):
        message = country('shanghai','china')
        self.assertEqual(message,'china-shanghai')
    
    def test_stat(self):  # 添加一个可选测试
        message = country('beijing','china',2000)
        self.assertEqual(message,'china-beijing-2000')

unittest.main()