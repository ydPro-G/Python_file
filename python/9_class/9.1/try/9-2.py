# 类
class Restaurant():
    """指出餐厅名字和菜品"""
    def __init__(self,restaurant_name,cuisine_type): #  特殊的方法（函数），三个形参，self相当于实例自己
        
        # 属性
        self.restaurant_name = restaurant_name # 餐厅名字
        self.cuisine_type = cuisine_type # 菜品

     # 方法
    def describe_restaurant(self): # 需要有形参self，让实例能够访问方法
        print("餐厅名字是" + self.restaurant_name.title() + ".")
        print("餐厅的菜品有" + self.cuisine_type + ".")

    def open_restaurant(self):
        print("餐厅正在营业中")



print("\n1")
# 实例1
restaruant = Restaurant('中华小当家','小笼包')
restaruant.describe_restaurant() 


print("\n2")
# 实例2
restaruant_2 = Restaurant('ruiXing Koffice','西餐')

print("restaurant name is " + restaruant_2.restaurant_name.title() + '.') # 访问实例的属性——实例名称.属性
print("cuisine type is " + restaruant_2.cuisine_type + ".") # Python先找到实例，再找到与这个实例相关联的属性，在类中引用这个属性时是self.属性

restaruant_2.describe_restaurant()# 调用方法——实例名称.类中方法



print("\n3")
# 实例3
restaruant_3 = Restaurant('自主餐厅','more')
restaruant_3.describe_restaurant()