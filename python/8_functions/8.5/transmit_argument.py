# 8.5 传递任意数量的实参

# 函数可从调用语句中收集任意数量的实参，使用*号

def make_pizza(*toppings): # *号让python创建了一个名为topping的空元组，将收到的所有值都封装到这个元组中
    """
    打印顾客点的所有配料
    """
    print(toppings)   # 元组不能和字符串一起使用

make_pizza('胡椒') #Python将实参封装到一个元组中，即使函数只收到一个值也如此
make_pizza('青椒','番茄酱') # 注意要调用函数!!


# 美化
def make_pizza_a(*stocks): # *号让python创建一个空元组
    """
    概述要制作的披萨
    """
    print("\nMakeing a pizza with the following toppings: ")  # 美化
    for stock in stocks: # for 循环
        print("- " + stock)  # 美化

make_pizza_a('大蒜')
make_pizza_a('火腿')







# 8.5.1 结合使用位置实参和任意数量实参
# 如何让任意数量的实参与位置实参，关键字实参一起使用？ 
# 在函数定义中将接纳任意数量实参的形参放在最后。Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后的一个形参中
print("\n8.5.1")

def make_pizza_b(size,*yuanliao): # python将收到的第一个值存储到形参size中，将其他所有值存储到元组中
    """
    描述要制作的pizza
    """
    print("pizza size is " + str(size) +  # str表明是字符串类型
           "-inch pizza with the following toppings:")
    for y in yuanliao:
        print("- " + y)

make_pizza_b(16,'胡椒') # 指定表示披萨尺寸的实参，根据需要指定任意数量的配料
make_pizza_b(20,'火腿','西红柿')









# 8.5.2 使用任意数量的关键字实参

# 不知道用户要传递给函数的信息，所以使用字典来存储用户要提供的信息，这样他们就能指定键-值对（用户除了固定的姓，名，还要个性的介绍自己

print("\n8.5.2")
# 要求提供名和姓，并允许用户根据需要提供任意数量的名称-值对
def build_profile(first,last,**user_info):   # 2个**号创建的是空字典，1个*号是空元组
    """
    创建一个字典，其中包含我们知道的有关用户的一切
    """
    profile = {}  # 函数体：创建一个空字典，存储用户简介
    profile['first_name'] = first # 将名加入这个profile字典
    profile['last_name'] = last   # 将姓加入这个profle字典
    for username,userinfo in user_info.items(): # 遍历字典user_info中的键值对
        profile[username] = userinfo # 将每个键-值对都加入到字典profile中

    return profile # 将字典profile返回给函数调用行
   


user_profile = build_profile('alis','cins',guan='22',sun='php') # 调用函数build_profile,向它传递名，姓和两个键-值对，将返回的profile字典存储在变量中

print(user_profile) # 打印这个变量

