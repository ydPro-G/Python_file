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

# import unittest
# from survey import AnonymousSurvey

# class TestAnonymousSurvey(unittest.TestCase): # 继承了unittest.TestCase
#     """针对AnonymousSurvey类测试"""

#     def test_store_single_response(self):
#         """测试单个答案存储"""
#         question = "What language did you first learn to speak?" # 设置一个变量存储问题
#         my_survey = AnonymousSurvey(question) # 实例 = 类(传递实参(变量))
#         my_survey.store_response('English') # 实例.方法(实参)
#         self.assertIn('English',my_survey.responses) # 实例.属性


#     def test_store_single_responses(self):
#         """测试多个答案"""
#         questions = "What language did you first learn to speak?"
#         my_surveys = AnonymousSurvey(questions)
#         responses = ['chinese','english','japanese']
#         for response in responses:
#             my_surveys.store_response(response)
        
#         for response in responses: # 使用循环确认每个答案都包含在my_surveys.responses中
#             self.assertIn(response,my_surveys.responses) # 再循环里将变量里的数据与属性里的数据对比

# unittest.main()










print('\n11.2.4')

# 11.2.4 方法setUp()
 # unittest.TestCase()类中包含方法setUp(设置),只需要创建这些对象一次，并在每个测试方法使用它们
 # 如果TestCase类中包含方法setUp()，python将先运行它，再运行各个以test_打头的方法

# 使用setUp()创建一个调查对象和一组答案，供方法使用



import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对类的测试"""

    def setUp(self):   # 如果要使用setUp()方法，那么之下的方法就必须包含在setUp方法中才可调用
        """创建一个调查对象和一组答案，供测试方法使用"""
        question = "What language did you first learn to speal?"# 创建一个调查对象
        self.my_survey = AnonymousSurvey(question) # 将这个变量存储到一个属性中           | 可以在这个类中的任何地方使用
        self.responses = ['English','Chinese','Japanese'] # 创建一个属性，存储答案列表    | 可以在这个类中的任何地方使用 

    def test_store_single_response(self):
        """测试单个答案保存"""
        self.my_survey.store_response(self.responses[0]) 
        self.assertIn(self.responses[0],self.my_survey.responses) 

    def test_store_three_responses(self):
        """测试三个答案保存"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

unittest.main()  

# 测试通过打印一个句点
# 测试引发错误打印一个E
# 测试导致断言失败打印一个F



