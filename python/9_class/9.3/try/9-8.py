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



# 实例1
user_one = User('小','明',16)

# 方法
user_one.describe_user()
user_one.greet_user()







print("\n9-8")
class Privileges():#新建一个类，将这个类的实例用作另一个类的属性
    """新建一个类，将这个类的实例用作另一个类的属性"""
    def __init__(self,privilege = '添加用户'): # 要将实例用作另一个类的属性必须要在形参或属性中指定值
        self.privilege = privilege
    
    def show_privileges(self):
        print("管理员的权限有：" + self.privilege)
messages = Privileges()
messages.show_privileges() # 注意要调用方法


class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.one = Privileges() #将类中的实例用作这个类中的属性

admin = Admin('X','M',15)
print(admin.one.show_privileges()) #因为python中print函数需要返回值，如果你在print函数中所放的函数没有返回值，那么print将会return None
admin.one.show_privileges() # 这里先在实例中查找属性，并调用该属性中关联的类的另一类的方法

# python中print函数需要返回值，如果你在print函数中所放的函数没有返回值，那么print将会return None
# 简单来说就是在show_privileges方法中print()已经输出了返回值，那么在实例中自然 return None










