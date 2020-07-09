import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对类的测试"""

    def setUp(self):   # 如果要使用setUp()方法，那么之下的方法就必须包含在setUp方法中才可调用
        """
        创建一个调查对象和一组答案，供测试方法使用
        """
        question = "What language did you first learn to speal?"# 创建一个调查对象

        self.my_survey = AnonymousSurvey(question) # 将这个变量存储到一个属性中           | 可以在这个类中的任何地方使用
        self.responses = ['English','Chinese','Japanese'] # 创建一个属性，存储答案列表    | 可以在这个类中的任何地方使用 

    def test_store_single_response(self):
        """测试单个答案保存"""
        self.my_survey.store_response(self.responses[0]) # 将答案属性的第一个答案存储到方法store_response中
        self.assertIn(self.responses[0],self.my_survey.store_response) # 对比答案属性与方法store_response，查看是否存储

    def test_store_three_responses(self):
        """测试三个答案保存"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

unittest.main()  