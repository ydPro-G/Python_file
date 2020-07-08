print('11.2.1')
 # 11.2.1  各种断言方法

  #  assertEqual(a,b)                 核实 a == b
  #  assertNotEqual(a,b)              核实a != b

  #  assertTrue(x)                    核实x为true
  #  assertFalse(x)                   核实x为False

  #  assertIn(item,list)              核实item在list中
  #  assertNotIn(item,list)           核实item不在list中







print('11.2.3')

# 11.2.3 测试 AnobymousSurvey类
 # 使用方法assertIn()来核实它包含在答案列表中

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase): # 继承了unittest.TestCase
    """针对AnonymousSurvey类测试"""

    def test_store_single_response(self):
        """测试单个答案存储"""
        question = "What language did you first learn to speak?" # 设置一个变量存储问题
        my_survey = AnonymousSurvey(question) # 实例 = 类(传递实参(变量))
        my_survey.store_response('English') # 实例.方法(实参)
        self.assertIn('English',my_survey.responses) # 实例.属性


    def test_store_single_responses(self):
        """测试多个答案"""
        questions = "What language did you first learn to speak?"
        my_surveys = AnonymousSurvey(questions)
        responses = ['chinese','english','japanese']
        for response in responses:
            my_surveys.store_response(response)
        
        for response in responses: # 使用循环确认每个答案都包含在my_surveys.responses中
            self.assertIn(response,my_surveys.responses) # 再循环里将变量里的数据与属性里的数据对比

unittest.main()