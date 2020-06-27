"""一个可用于表示汽车的类"""  # 一个模块级文档字符串

class Car():

    def __init__(self,make,model,year):

        # 属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 里程数

    def get_descriptive_name(self):
        """返回简洁的描述"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """指出汽车里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        """将里程表设置为特定值，并禁止回调"""
        if self.odometer_reading >= mileage:
            self.odometer_reading = mileage
        else:
            print("You can`t roll back on odometer!")

    def increment_odometer(self,miles):
        """将里程表读数增加指定的值"""
        self.odometer_reading += miles



class Battery():
    """模拟电动车电瓶的简单尝试"""
    def __init__(self,battery_size=70): # 默认形参是60，但是判断条件里是70和85，所以range变量一直没有被赋值
        """初始化电瓶属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + '-KWh battery.')

    def get_range(self):
        """打印续航里程数消息"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "里程数是" + str(range)
        message += "还可以跑很久。"
        print(message)


class ElectricCar(Car):
    """模拟电动车"""
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
