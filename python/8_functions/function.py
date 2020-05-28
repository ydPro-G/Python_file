# 8.1 定义函数
print("/n8.1")

def greet_user():  # 使用关键字def来告诉Python定义一个函数——函数定义：向python指出函数名，可能在括号内指出函数为完成任务需要什么样信息
    """显示简单的问候语"""  # 文档字符串的注释，描述函数时做什么的，三个引号扩起，生成有关程序中函数的文档
    print("hello!")# 跟在函数：后面的所有缩进行构成了函数体，print是唯一一行代码

greet_user()# 打印Hello，调用函数，依次指定函数名以及用括号括起的必要信息。






# 8.1.1 向函数传递信息
print("\n8.1.1")

def greet_user1(username): # 函数接受代码greet_user1('jeese')传递的信息
    """显示简单的用户语"""
    print("Hello, " + username.title() + "!")

greet_user1('jeese') # 代码greet_user1('jeese')调用函数greet_user(),并向它提供执行print语句所需的信息
greet_user1('sourch') # 可以根据需要调用函数greet_user1()任意次，无论传入什么都会生成相应的输出