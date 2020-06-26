# 9.4 导入类
# 将类存储到模块中，然后在主程序中导入所需的模块


#9.4.1 导入单个类
from car import Car # 打开模块car,并导入其中Car类

my_new_car = Car('audi','a4',2016)

print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23

my_new_car.read_odometer()