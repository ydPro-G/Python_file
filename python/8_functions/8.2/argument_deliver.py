# 8.2 传递实参
# 1.位置实参：实参的顺序与形参的顺序相同；
# 2.关键字实参，每个实参都由变量名和值组成；
# 3.列表和字典也可以使用


# 8.2.1 位置实参
# 将函数调用中的每个实参关联到函数定义中的一个形参；
# 最简单关联：基于实参的顺序——位置实参
# 按顺序将函数调用中的实参关联到函数定义中相关的形参
print("\n8.2.1")

def describe_pet(animal_type,pet_name):  #位置实参：实参按照形参的顺序传递给函数的形参
    """显示宠物的信息"""
    print("\nI have a  " + animal_type + ".")
    print("My " + animal_type + " name is " + pet_name.title() + ".")

describe_pet('hamster','harry')
describe_pet('dog','willie') # 调用函数多次：可以根据需要调用函数任意次，Python将实参关联到形参







# 8.2.2 关键字实参

# 关键字实参是传递给函数的名称—值对
print("\n8.2.2")

def describe_pets(animal_types,pet_names):
    """显示宠物的信息"""
    print("\nI have a " + animal_types + ".")
    print("My " + animal_types + " name is " + pet_names.title() + ".")

describe_pets(animal_types='hamster',pet_names='harry') #向python明确的指出了各个实参对应的形参，将实参分别储存在形参中






# 8.2.3 默认值

# 使用默认值时，在形参列表中必须先列出没有默认值的形参，让python能正确解读位置实参

# 在编写函数时，可给每个形参指定默认值

# 在调用函数中给形参提供实参时，Python将使用指定的实参值，否则，将使用形参的默认值
print("\n8.2.3")
def describe_pet_2(pet_name_2,animal_type_2='dog'): # 给形参指定默认值
    print("\nI have a " + animal_type_2 + ".")
    print("My " + animal_type_2 + " name is " + pet_name_2.title() + ".")

describe_pet_2(pet_name_2='willie') #  调用这个函数时，如果没有给这个形参指定值，Python将把这个形参设置为默认值dog
describe_pet_2(pet_name_2='jesee')  #






# 8.2.4 等效的函数调用
print("\n8.2.4")
# 鉴于可混合使用位置实参，关键字实参，默认值，通常有多种等效的函数调用方式







# 8.2.5 避免实参错误
print("/n8.2.5")
# 提供的实参多余或少于函数完成其工作所需的信息时，将出现实参不匹配错误

