# 9.3 继承
# 一个类可以继承另一个类
# 一个类继承另一个类时，它将自动获得另一个类的所有属性和方法
# 原有的类称为父类，新类称为子类
# 子类继承其父类的所有属性和方法，同时还可以定义自己的属性和方法









# 9.3.1 子类的方法_init_()
print('\n9.3.1')

# 创建子类的实例时，python首先要给父类的所有属性赋值。子类的方法_init_()，需要父类施以援手

# ElectricCar（电车）继承Car类

class Car():
    """汽车"""

    def __init__(self,make,model,year):

        # 属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # 方法
    def get_descriptive_name(self): # 车辆信息
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
 

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('No!')

    def increnent_odometer(self,miles):
        self.odometer_reading += miles

    


# 创建子类时，父类必须包含在当前文件中，且位于子类前面

class ElectricCar(Car): # 定义了子类，子类继承父类，括号内指定父类名称
    """电动车"""
    def __init__(self,make,model,year): # 方法_init_()接受创建Car实例所需的信息
        """初始化父类属性"""
        super().__init__(make,model,year) # super()，让父类和子类关联起来，让python调用父类的方法_init_()，让子类实例包含父类的所有属性，父类也被称为超类(super)


my_tesla = ElectricCar('电动车','电动',2016) # 创建一个子类的实例，存储到变量中。 这行代码调用子类中定义的方法_init_()，后者让Python调用父类Car中定义的方法_init_()，我们提供实参
print(my_tesla.get_descriptive_name())












# 9.3.3 给子类定义属性和方法
print('\n9.3.3')

    

 
