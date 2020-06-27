# 9.4.2 在一个模块存储多个类
# 可在一个模块中存储任意数量的类
from car import ElectricCar

my_tesla = ElectricCar('tesla','models',2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 大部分逻辑被隐藏再一个模块中