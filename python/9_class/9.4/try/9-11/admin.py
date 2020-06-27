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











class Privileges():#新建一个类，将这个类的实例用作另一个类的属性
    """新建一个类，将这个类的实例用作另一个类的属性"""
    def __init__(self,privilege = '添加用户'): # 要将实例用作另一个类的属性必须要在形参或属性中指定值
        self.privilege = privilege
    
    def show_privileges(self):
        print("管理员的权限有：" + self.privilege)



class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.one = Privileges() #将类中的实例用作这个类中的属性











