class Employee():
    """获取一个雇员的名字和年薪"""
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = 0


    def give_raise(self,increase=''):
        if increase:
            total =self.salary + increase   
        else:
            self.salary = self.salary + 5000
            total = self.salary
        return total

