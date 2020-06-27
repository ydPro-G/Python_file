# 用户
class User():
    """用户信息与问候用户"""

    def __init__(self,first_name,last_name,age):

        # 属性
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
 
        # 方法
    def describe_user(self):
        print("用户名字是" + self.first_name + self.last_name) 
        print("用户年龄是" + str(self.age) + ".")

    def greet_user(self): 
        print("欢迎光临," + self.first_name + self.last_name)