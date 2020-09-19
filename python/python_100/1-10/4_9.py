# 4.编写一个程序，从控制台接受一个以逗号为分割的数字序列，并根据输入输出一个列表和元组，以逗号分割
num = input().split(',')
lst = tuple(num) #input.tuple ()方法可以将 list 转换为 tuple

print(num)
print(lst)

# 5 定义有两个方法的类，从控制台输入获取字符串，打印字符串，打印大写字符串，包含简单的测试函数来测试类方法

class IOstring():
    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())

xx = IOstring()
xx.get_string()
xx.print_string()


# 6 编写一个程序，根据给定的公式计算并打印这个值
# Q = Square root of [(2 _ C _ D)/H]
# C is 50 H is 30 , D是一个变量，其值以,分割的序列输入到程序中
from math import sqrt
c = 50
d = 30

 def calc(D):
     return sqrt((2*c*D)/H)


