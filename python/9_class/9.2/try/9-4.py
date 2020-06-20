# 类
class Restaurant():
    """指出餐厅名字和菜品"""
    def __init__(self,restaurant_name,cuisine_type):
        
        # 属性
        self.restaurant_name = restaurant_name # 餐厅名字
        self.cuisine_type = cuisine_type # 菜品
        self.number_served = 0 # 服务人数

     # 方法
    def describe_restaurant(self):
        print("餐厅名字是" + self.restaurant_name.title() + ".")
        print("餐厅的菜品有" + self.cuisine_type + ".")

    def open_restaurant(self):
        print("餐厅正在营业中")

    def set_number_served(self,user_number):
        self.number_served = user_number # 修改属性的值

    def increment_number_served(self,number_add):
        self.number_served += number_add # 递增属性值
 




# 直接修改属性的值
restaurant = Restaurant('拉面馆','拉面')
print(restaurant.restaurant_name + '有' + restaurant.cuisine_type + ',服务人数有' + str(restaurant.number_served))  # 不带括号时调用的是这个函数本身 
                                                                    # 如果带括号，因为没有相应参数，会报错
restaurant.number_served = 1 # 直接修改属性的值（实例.属性 = ）
print('服务人数有' + str(restaurant.number_served))


# 通过方法修改属性的值
restaurant.set_number_served(2) 
print('服务人数有' + str(restaurant.number_served))


# 通过方法递增属性的值
restaurant.increment_number_served(1)
print('服务人数有' + str(restaurant.number_served))





# 