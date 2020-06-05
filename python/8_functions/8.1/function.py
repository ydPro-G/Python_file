#  函数
#def good_users(names):                         #  |   函数定义与形参
#    """向列表中每位用户都发出简单的问候"""         # | 这是文档字符串
#    for name in names:  # 函数遍历收到的列表        |
#        msg = "Hello, " + name + "."             #|
#        print(msg)                               #|   这些是函数体
    
#username = ['han','tian','guo']   #定义一个用户列表
#good_users(username) #                            | 这是函数调用与实参    调用函数，并将这个列表传递给它












# 8.1 定义函数
print("/n8.1")

def greet_user():  # 使用关键字def来告诉Python定义一个函数——函数定义：向python指出函数名，可能在括号内指出函数为完成任务需要什么样信息
    """显示简单的问候语"""  # 文档字符串的注释，描述函数时做什么的，三个引号扩起，生成有关程序中函数的文档
    print("hello!")# 跟在函数：后面的所有缩进行构成了函数体，print是唯一一行代码

greet_user()# 调用函数，依次指定函数名以及用括号括起的必要信息。






# 8.1.1 向函数传递信息
print("\n8.1.1")

def greet_user1(username): # 函数定义：函数接受代码greet_user1('jeese')传递的信息
    """显示简单的用户语"""
    print("Hello, " + username.title() + "!")

greet_user1('jeese') # 函数调用：代码greet_user1('jeese')调用函数greet_user(),并向它提供执行print语句所需的信息
greet_user1('sourch') # 可以根据需要调用函数greet_user1()任意次，无论传入什么都会生成相应的输出






# 8.1.2 实参和形参
print("/n8.1.2")
#  greet_user(username)中username是一个形参；形参时函数完成其工作所需的一项信息，实参传递给函数的值被储存在形参中
#  greet_user('jesse')中jesse是一个实参；实参是调用函数时传递给函数的信息，调用函数时，要让函数使用的信息放在括号内


# 过程：在greet_user('jesse')中，将实参'jesse'传递给函数greet_user(),这个值被储存在username()中
# 抽象与具体