# 9.4 导入类
# 将类存储到模块中，然后在主程序中导入所需的模块


#9.4.1 导入单个类
from car import Car # 打开模块car,并导入其中Car类

my_new_car = Car('audi','a4',2016)

print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23

my_new_car.read_odometer()










# 9.4.2 在一个模块存储多个类
# 可在一个模块中存储任意数量的类
# from car import ElectricCar

# my_tesla = ElectricCar('tesla','models',2019)

# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# 大部分逻辑被隐藏再一个模块中










# 9.4.3 从一个模块中导入多个类
print("\n9.4.3")

from car import Car, ElectricCar # ，号分隔

my_beetle =Car('a','beetle',2017) # Car类
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2018) # ElectricCar类
print(my_tesla.get_descriptive_name())













# 9.4.4 导入整个模块
print("\n9.4.4")
import car # 导入整个car模块

one = car.Car('one','one',2010) # 模块.类
print(one.get_descriptive_name()) 


two = car.ElectricCar('two','two',2020) # 模块.类
print(two.get_descriptive_name())









# 9.4.5 导入模块中的所有类
print("\n9.4.5")
#from car import * # 不推荐这种导入方式










# 9.4.6 在一个模块中导入另一个模块
# 不同的类储存在不同的模块
print("\n9.4.6")
from car import Car # car 模块 Car类
from electric_car import ElectricCar

th = Car('T','H',2013)
print(th.get_descriptive_name())


td = ElectricCar('E','L',2015)
print(td.get_descriptive_name())
