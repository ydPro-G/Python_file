# 用户
class User():
    """用户信息与问候用户"""

    def __init__(self,first_name,last_name,age):

        # 属性
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0 # 登录次数为0
 
        # 方法
    def describe_user(self):
        print("用户名字是" + self.first_name + self.last_name)
        print("用户年龄是" + str(self.age) + ".")

    def increment_login_attempts(self,number):
        self.login_attempts += number  # 将属性值递增

    def reset_login_attempts(self,zero):  # 重置为0
        self.login_attempts = zero



# 实例1
user = User('小','明',16)

# 方法
user.describe_user()

user.increment_login_attempts(1) #方法需要传递实参，所以带()
print(str(user.login_attempts)) # 参数直接调用就好

user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.increment_login_attempts(1)
print(str(user.login_attempts))

user.reset_login_attempts(0) # 重置为0
print(user.login_attempts)














