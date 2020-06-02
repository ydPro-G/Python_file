# 8.3返回值；函数可以处理数据并返回一个或一组值。
# 函数返回的值被称为返回值。
# 使用return语句将值返回到调用函数的代码行

# 8.3.1  返回简单值
print("8.3.1")
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name + " " + last_name # 将结果存储到变量full_name中
    return full_name.title() #  将变量转换为首字母大写并将结果返回到函数调用行

musician = get_formatted_name('jimi','hendrix') # 调用返回值的函数时，提供一个变量，用于存储返回的值，将返回值存储在提供的变量中
print(musician)





# 8.3.2 让实参变成可选的
# 让使用函数的人只需在必要时才提供额外的信息
# 使用默认值来让实参变成可选的
print("\n8.3.2")

def get_formatted_names(first_names,middle_name,last_names): # 名，中间名，姓
    """返回整洁的姓名"""
    full_names = first_names + ' ' + middle_name + ' ' + last_names # 将结果储存在full_names
    return full_names.title() # 将结果也就是fuu_names返回到函数调用行
musicians = get_formatted_names('join','han','ser') # 提供名，中间名，姓
print(musicians)

#  并非所有人都拥有中间名
#  让中间名变为可选，可给实参middle_name指定一个默认值——空字符串
#  在用户没有提供中间名时不使用这个实参
def get_formatted_name_optional(first_n,last_n,middle_n=''): # 中间名给出实参，
    """返回整洁的姓名"""
    if middle_n: #检查是否提供了中间名，将非空字符串解读为True(提供了中间名就是非空)，如果调用中提供了中间名，if middle_n 为True，执行下面的代码行
        full_n = first_n + ' ' + middle_n + ' ' + last_n
    else: # 没有提供中间名为Flase,if检测未通过，执行else
        full_n = first_n + ' ' + last_n
    return full_n.title()

musician_m = get_formatted_name_optional('jimi','hendix')
musician_p = get_formatted_name_optional('han','nai','se')

print(musician_m)
print(musician_p)











# 8.3.3  返回字典
print("\n8.3.3")
def build_person(first_name_d,last_name_d): # 函数接受名和姓
    """返回字典"""
    person = {'first': first_name_d,'last': last_name_d}# 将这些值封装到字典中
    return person # 返回字典

musician_a = build_person('jimi','hansd')
print(musician_a)

# 储存年龄
def build_persons(first_name_e,last_name_e,age=''): # 在函数定义中，新增一个可选形参age，将其默认值设置为空字符串，调用中包含这个形参的值，则把这个值存储到字典中
    """年龄为可选项"""
    if age:
        persons = {'frist_name_e': first_name_e,'last_name_e': last_name_e,'age': age}
    else:
        persons = {'frist_name_e': first_name_e,'last_name_e': last_name_e}
    # person = {'frist_name_e': first_name_e,'last_name_e': last_name_e} 默认一直输出，这个好一点
    # if age:
    #    person['age'] = age  如果age非空则函数包含年龄，如果为空则不包含
    return str(persons).title()

a = build_persons('a','b')
b = build_persons('c','d',20)

print(a)
print(b)










# 8.3.4 结合使用函数和while循环
# 可将函数和之前学习的任何Python结构结合起来使用
print("\n8.3.4")

def g_f_n(f_name,l_name):
    """返回整洁的姓名"""
    full_na = f_name + ' ' + l_name
    return full_na.title()
# 这是一个无限循环
while True: # 让用户输入姓名，依次提示用户输入名和姓
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_names = input("First name: ")
    if f_names == 'q':
        break
    l_names = input("Last name: ")
    if l_names == 'q':
        break# 告诉用户退出

    formatted_name = g_f_n(f_names,l_names)
    print("\nHell, " + formatted_name + "!")
