# 8.5 传递任意数量的实参

# 函数可从调用语句中手机任意数量的实参

def make_pizza(*toppings): # *toppings中的*号让python创建一个名为toppings的空元组，将收到的所有值都封装到这个元组中
    """
    打印顾客点的所有配料
    """
    print(toppings)# 函数体

make_pizza('pisaaa')
make_pizza('pisaa','pisab','pisac')