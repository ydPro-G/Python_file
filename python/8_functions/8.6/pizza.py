def make_pizza(size,*toppings): # 函数定义
    """
    描述要制作的披萨
    """
    print("匹萨尺寸是：" + str(size) + "，要添加的配料是：")
    for topping in toppings:
        print("- " + topping)  # 函数体

def two(sizes):
    print(sizes)