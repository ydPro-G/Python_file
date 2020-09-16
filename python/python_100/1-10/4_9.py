# 4.编写一个程序，从控制台接受一个以逗号为分割的数字序列，并根据输入输出一个列表和元组，以逗号分割
num = input().split(',')
lst = tuple(num) #input.tuple ()方法可以将 list 转换为 tuple

print(num)
print(lst)

# 5