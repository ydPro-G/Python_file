# 4.编写一个程序，从控制台接受一个以逗号为分割的数字序列，并根据输入输出一个列表和元组，以逗号分割
num = input().split(',')
lst = tuple(num) #input.tuple ()方法可以将 list 转换为 tuple

print(num)
print(lst)

# 5 定义有两个方法的类，从控制台输入获取字符串，打印字符串，打印大写字符串，包含简单的测试函数来测试类方法

calss Iostring():
    def get_string(self):
        self = input()
    def print_string(self):
        print(self.upper())

xx = IOstring()
xx.get_string()
xx.print_string()



