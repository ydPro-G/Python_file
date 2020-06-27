from user_a import User # 一个模块导入另一个模块


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