# 用户
class User():
    """用户信息与问候用户"""

    def __init__(self,first_name,last_name,age):# self它是一个 指向 实例本身 的  引用

        # 属性
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
 
        # 方法
    def describe_user(self):
        print("用户名字是" + self.first_name + self.last_name) #实参的值被储存到形参中，形参中的值被存储到变量中，变量通过self可以被类中方法使用
        print("用户年龄是" + str(self.age) + ".")

    def greet_user(self): # 这些方法不需要别的信息，只需要self让实例能访问这些方法
        print("欢迎光临," + self.first_name + self.last_name)



# 实例1
user_one = User('小','明',16)

# 方法
user_one.describe_user()
user_one.greet_user()


print("\n2")
# 实例2
user_two = User('小','赵',20)
user_two.describe_user()
user_two.greet_user()