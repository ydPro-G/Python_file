# 用while里用户获得的输入作为形参，return的bi'da

def get_name(first_name,last_name):#函数通过形参接受数据
    full_name = first_name + last_name # 将数据合二为一并将合二为一的结果储存在一个变量中
    return full_name # 退出函数，并给调用方返回一个表达式/结果，也可以把这个变量值的值转换下

# 从用户那里获取名字
while True:
    print("enter 'q' quit")
    f_name = input("First name is :")
    if f_name == 'q':  # 定义退出条件
        break
    l_name = input("Last name is :")
    if l_name == 'q':
        break

    name = get_name(f_name,l_name) # 接受return返回的表达式，通过表达式计算值，为了储存这个返回的值（这个值在return中就计算完了）需提供一个变量
    print("Name is " + name)
