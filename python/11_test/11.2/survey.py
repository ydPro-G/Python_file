# 11.2  测试类



print('11.2.1')
 # 11.2.1  各种断言方法

  #  assertEqual(a,b)                 核实 a == b
  #  assertNotEqual(a,b)              核实a != b

  #  assertTrue(x)                    核实x为true
  #  assertFalse(x)                   核实x为False

  #  assertIn(item,list)              核实item在list中
  #  assertNotIn(item,list)           核实item不在list中









print('\n11.2.2')
# 11.2.2 一个要测试的类
 # 帮助管理匿名调查的类

class AnonymousSurvey():
    """收集匿名调查问卷的答案"""
    
    def __init__(self,question):
        """存储一个问题,并为存储答案做准备"""
        self.question = question
        self.responses = []

    
    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self,new_response):
        """存储单份调查问卷"""
        self.responses.append(new_response)
    
    def show_results(self):
        """显示收集到的所有调查问卷"""
        print('Survey results:')
        for response in self.responses:
            print('- ' + response)

# one = AnonymousSurvey('a is a ?')
# one.show_question() # 显示问题

# one.store_response('a') # 存储答案
# one.store_response('b') # 存储答案
# one.show_results() # 显示所有答案