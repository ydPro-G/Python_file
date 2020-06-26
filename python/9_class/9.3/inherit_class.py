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
        super().__init__(make,model,year) # super()，让父类和子类关联起来，让python调用子类的父类的方法_init_()，让子类实例包含父类的所有属性，父类也被称为超类(super)


my_tesla = ElectricCar('电动车','电动',2016) # 创建一个子类的实例，存储到变量中。 这行代码调用子类中定义的方法_init_()，后者让Python调用父类Car中定义的方法_init_()，我们提供实参
print(my_tesla.get_descriptive_name())












# 9.3.3 给子类定义属性和方法
print('\n9.3.3')
# 一个类继承另一个类后，可添加区分子类和父类所需的新属性和方法
# 添加一个电动汽车特有属性(电瓶)，以及一个描述该属性的方法
class EleC(Car):
    """添加子类的新属性和方法"""
    def __init__(self,make,model,year):
        """新属性：电池容量
        初始化父类的属性，再初始化电动汽车特有属性
        """
        super().__init__(make,model,year)



        # 定义新属性，根据Elec类创建的所有实例都包含这个属性，但父类所有实例都不包含它
        self.battery_size = 70 # 电池容量70



        # 新方法
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This cai has a " + str(self.battery_size) + "-KWH battery.")



my_teslas = EleC('tesla','models',2016)
print(my_teslas.get_descriptive_name())
my_teslas.describe_battery() # 调用新方法








# 9.3.4 重写父类的方法

# 对于父类的方法，只要不符合子类的要求就可以重写
# 可在子类中定义这样一个方法，它与要重写的父类方法同名，这样，Python将忽略这个父类方法，而只关注这个子类方法
print('\n')












 
# 9.3.5 将实例用作属性

# 新建一个类，将这个类的实例用作另一个类的属性

# 可以将类的一部分作为一个单独的类提取出来，将大型类拆分为多个协同工作的小类
# 将小类的实例用作大类的一个属性
print('\n9.3.5')

class Battery():
	"""一次模拟电动汽车电瓶的简单尝试"""
	def __init__(self,battery_size=70):
		#battery_size为形参
		"""初始化电瓶的属性"""
		self.battery_size=battery_size
	def describe_battery(self):
		"""打印一条描述电瓶容量的信息"""
		print("This car has a "+str(self.battery_size)+"-kwh battery.")
		#方法describe_battery被移到了Barrery类中
	def get_range(self):
		"""打印一条信息，指出电瓶的续航里程"""
		if self.battery_size==70:
			range=240
		elif self.battery_size==85:
			range=270
		message="This car can go approximately "+str(range)
		message+=" miles on a full charge."
		print(message)   # 这是一个方法，这不是一个实例
            


      
    
    
    


class ElCar(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.batterys = Battery() #这个类现在被用作实例，添加了一个属性，创建一个新的Battery实例，将该实例存储在属性中，每当方法init_被调用,都将执行该操作，因此每一个子类实例都包含一个自动创建的Battery实例，


my_t = ElCar('teals','model`s',2019)
print(my_t.get_descriptive_name())#这里先在实例中查找属性，并调用该属性中关联的类的另一类的方法
my_t.batterys.get_range()









# 9.3.6 模拟实物

# 将里程数留在小类中，通过向它传递一个参数，如car_model,在这种情况下，方法get_range（）将根据电瓶容量和汽车类型报告续航里程数

