# 9.2  使用类和实例
# 编写好类后，大部分时间都将花在使用根据类创建的实例上
# 一个重要任务：修改实例的属性
# 可以直接修改实例的属性，也可以编写方法以特定的方式进行修改


# 9.2.1 Car类 
print("\n9.2.1")
# 存储有关信息，还有一个汇总这些信息的方法

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year): # |定义方法_init_(),形参self,另外三个形参:make,model,year
        """初始化描述汽车的属性"""        # | 方法_init_()接受这些形参的值，将他们存储在根据这个类创建的实例的属性中 

        # 属性
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self): # 定义了一个方法
        """返回整洁的描述性信息"""
        # 方法
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model # 使用属性创建一个字符串
        return long_name.title()   # 使用return 返回汇总信息

my_new_car = Car('audi','a4',2016) # 根据Car类创建了一个实例，将其存储到变量中
print(my_new_car.get_descriptive_name()) # 实例.方法,调用方法







# 9.2.2 给属性指定默认值
# 添加一个随时间变化的属性，存储汽车的总里程数
# 类中的每个属性都必须有初始值
# 设置默认值时，在方法_init_(),指定这种初始值时可行的
# 如果某个属性设置了默认值，就无需包含为它提供初始值的形参
print("\n9.2.2")
class   Cars():
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year # 可以获取输入的值也可以自定义值，两者的不同就是，属性设置默认值后就可以不用有形参了，形参的作用在于获取实参
        self.odometer_reading = 0 # 属性设置了默认值，就无需有为它提供初始值的形参了

    def get_descriptive_names(self):
        long_names = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_names.title()

    def read_odometer(self):
        """打印一条指出汽车里程的信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.") # 调用属性时直接获取默认值

my_new_cars = Cars('baoma','a3',2020)
print(my_new_cars.get_descriptive_names()) # 方法不要忘记带()
my_new_cars.read_odometer() # 实例.方法








# 9.2.3 修改属性的值
print("\n9.2.3")
# 三种方法修改属性的值
# 1.通过实例直接进行修改
# 2.通过方法进行设置
# 3.通过方法进行递增（增加特定的值）

# 1.直接通过实例修改属性的值
print("9.2.3.1")
class   Carss():
    def __init__(self):
        """初始化描述汽车的属性"""
        self.odometer_readings = 1


    def read_odometers(self):
        """打印一条指出汽车里程的信息"""
        print("This car has " + str(self.odometer_readings) + " miles on it.")

my_car = Carss()
my_car.read_odometers()
my_car.odometer_readings = 2  # 直接修改属性的值，这里修改的是属性的值！！！
my_car.read_odometers() # 这里调用的是方法，不是属性！！
















# 2.通过方法修改属性的值
# 有一个更新属性的方法，就无需直接访问属性，将值传递给一个方法，由它在内部更新
print("\n9.2.3.2")
class   Carsa():

    def __init__(self): # 属性已指定默认值，所以这里不用有odometer_readings形参
        """初始化描述汽车的属性"""
        self.odometer_readings = 1 # 因为这里给属性指定了默认值，所以不需要有形参

    def read_odometers(self):
        """打印一条指出汽车里程的信息"""
        print("This car has " + str(self.odometer_readings) + " miles on it.")


    def update_odometer(self,mileage): # 添加一个方法，方法接受一个值
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_readings: # 如果实参传来的数值大于等于原始数值就将值传递给方法
            self.odometer_readings = mileage # 将值存储到需要更改的方法中
        else: # 如果值小于就弹出提示禁止修改
            print("禁止修改") 
        
my_car = Carsa() # 实例必须先指定类，才能使用类！！！
my_car.update_odometer(23) # 调用这个方法，向它提供实参，这个实参被存储到要修改的方法中
my_car.read_odometers()
my_car.update_odometer(10)     # 提示禁止修改












# 3.通过方法对属性的值进行递增
# 将属性值递增特定的量，而不是将其设置为全新的值
# 一辆二手车，购买到登记期间增加了100英里
print("\n9.2.3.3")

class Car_b():
    def __init__(self,make_b,model_b,year_b):
        """汽车属性"""

        #属性
        self.make_b = make_b
        self.model_b = model_b
        self.year_b = year_b
        self.odometer_reading_b = 0

        #方法
    def get_messages(self):   # 方法和方法缩进一致！！！！
        zong = str(self.year_b) + ' ' + self.make_b + ' ' + self.model_b
        return zong.title()

    def read_odometer_b(self):
        """打印一条汽车里程数"""
        print("The car has " + str(self.odometer_reading_b) + ".")


    def update_odometer_b(self,add):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """

        if add >= self.odometer_reading_b:
                self.odometer_reading_b = add
        else:
                print("禁止修改")
        
    def increment_odometer(self,miles_b): # 新增一个方法，接受一个数字，将其加入到属性——self.odometer_b中 
        """将里程表读数增加指定的量"""
        self.odometer_reading_b += miles_b # 将获取到的实参的数字加入到属性self.odometer_reading_b中



# 实例
my_used_car = Car_b('audi','A1',2013) # 创建一个实例
print(my_used_car.get_messages())

my_used_car.update_odometer_b(23500) # 调用方法update，更新属性self.odometer_reading_b
my_used_car.read_odometer_b()

my_used_car.increment_odometer(100) # 调用方法increment，并加入到属性self.odometer_reading_b中
my_used_car.read_odometer_b()


    

