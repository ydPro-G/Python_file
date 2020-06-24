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








print('\n9-7')
class Admin(User):
    """继承User类"""
    def __init__(self,first_name,last_name,age,privileges): # 方法
        super().__init__(first_name,last_name,age) # 特殊方法

        self.privileges = privileges #添加一个属性用来储存字符串组成的列表

    def show_privileges(self): #方法：显示管理员权限
        print('管理员的权限有：' + self.privileges)


admins = Admin('小','明',20,'添加用户') # 一个实例,调用方法show_privileges
print(admins.show_privileges())

    