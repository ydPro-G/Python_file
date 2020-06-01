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
