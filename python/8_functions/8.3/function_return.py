# 8.3返回值；函数可以处理数据并返回一个或一组值。返回的值被称为返回值。
# 使用return语句将  值  返回   到   调用函数   的   代码行






# 8.3.1  返回简单值
print("8.3.1")

def sum( arg1, arg2 ):#函数通过形参接受数据
   # 返回2个参数的和."
   a = arg1 + arg2# 将数据合二为一并将合二为一的结果储存在一个变量中
   print(a)  # 有一个print所以输出a，同时这个a的结果也被传给变量abc
   return a  # 将变量a返回给函数调用行的变量
 
# 调用sum函数
abc = sum( 10, 20 ) # 调用函数sum，并向函数传递实参的数据，运行函数体，然后将计算结果返回给abc，输出abc
print(abc)
















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


#  让中间名变为可选，可给实参middle_name指定一个默认值——空字符串
#  在用户没有提供中间名时不使用这个实参
def get_formatted_name_optional(first_n,last_n,middle_n=''): 
    if middle_n:                                             # 非空执行
        full_n = first_n + ' ' + middle_n + ' ' + last_n
    else:                                                      
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

# 储存年龄（字典实参可选）
def build_persons(first_name_e,last_name_e,age=''): # 在函数定义中，新增一个可选形参age，将其默认值设置为空字符串，调用中包含这个形参的值，则把这个值存储到字典中
    """年龄为可选项"""
    if age:
        persons = {'frist_name_e': first_name_e,'last_name_e': last_name_e,'age': age}
    else:
        persons = {'frist_name_e': first_name_e,'last_name_e': last_name_e}
    # person = {'frist_name_e': first_name_e,'last_name_e': last_name_e} 默认一直输出，这个好一点
    # if age:   非空才执行
    #    person['age'] = age  如果age非空则函数包含年龄，如果为空则不包含
    return str(persons).title()

a = build_persons('a','b')
b = build_persons('c','d',20)

print(a)
print(b)










# 8.3.4 结合使用函数和while循环
# 可将函数和之前学习的任何Python结构结合起来使用
# 单独开一个



    




