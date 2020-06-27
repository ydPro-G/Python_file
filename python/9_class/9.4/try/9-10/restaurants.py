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











print("\n9-6")

class IceCreamStand(Restaurant):
    """冰淇凌子类"""
    def __init__(self,restaurant_name,cuisine_type,*flavors):
        """初始化父类属性"""
        super().__init__(restaurant_name,cuisine_type) # 只填写父类的属性，不用填写self，初始化父类属性

        """添加一个属性，存储各种口味的冰淇淋"""
        self.flavors = flavors

    def show(self):
        for fl in self.flavors:
            print("喜欢的冰淇淋有：" + fl)



