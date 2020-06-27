""""一组表示电动汽车的类"""

from car import Car #

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
