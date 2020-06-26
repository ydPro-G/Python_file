class Car():
	def __init__(self,make,model,year):
		"""初始化描述汽车的属性"""
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0
		self.miles=0
	def get_desprective_name(self):
		"""返回整洁的描述性信息"""
		long_name=str(self.year)+' '+self.make+' '+self.model
		return long_name.title()
	def read_odometer(self):
		"""打印条指出汽车里程的消息"""
		print("This car has "+str(self.odometer_reading)+" miles on it.")
	def update_odometer(self,mileage):
		"""
		将里程表读数设置为指定的值
		禁止将里程表读数往回调
		"""
		if mileage>=self.odometer_reading:
			self.odometer_reading=mileage
			
		else:
			print("You can't roll back an odometer!")
	def increment_odometer(self,miles):
		"""将里程表读数增加指定的量"""
		if miles>=self.miles:
			self.odometer_reading+=miles
		else:
			print("You can't add the miles which is negative number!")
	def fill_gas_tank(self):
		print("This car have a  gas tank")



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
		print(message)
	def upgrade_battery(self): # 如果不是85修改为85
		if self.battery_size!=85:
			self.battery_size=85




class ElectricCar(Car):
	def __init__(self,make,model,age):
		super(ElectricCar,self).__init__(make,model,age)
		self.battery=Battery()
		#创建一个新的Battery实例，并将这个实例存储在属性self.battery中
	def fill_gas_tank(self):
		print("This car doesn't have a gas tank!")
		#对父类方法进行重写
my_elsctic=ElectricCar('tesla','model s',2016)



print(my_elsctic.get_desprective_name())
my_elsctic.battery.describe_battery()
my_elsctic.battery.get_range()
my_elsctic.battery.upgrade_battery()
my_elsctic.battery.get_range()
my_elsctic.fill_gas_tank()
