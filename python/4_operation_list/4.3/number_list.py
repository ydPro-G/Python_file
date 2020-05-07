#   4.3创建数值列表
print("4.3.1")
#   函数range()从指定的第一个值开始打印，到指定的最后一个值前停止（不包括最后一个值（5
for value in range(1,5):
    print(value)

#   使用range（）创建数字列表
print("\n4.3.2")
#   使用函数list()将range()的结果直接转换为列表，如果将range()作为list()的参数，输出将作为一个数字列表
numbers = list(range(1,6))
print(numbers)
#   使用函数range()时，可指定步长（最后一个2就是指定的步长，递增+2，-2就是递减-2）
even_numbers = list(range(2,11,2))
print(even_numbers)
print("\n")
#   创建一个列表，包含10个整数（1-10）的平方，在python中，**表示乘方运算
squares = []
#   使用函数range()让python遍历1-10的值
for value_2 in range(1,11):
#   将新计算得到的平方值附加到列表squares中
    squares.append(value_2**2)
print(squares)


#   4.3.3对数字列表执行简单的统计计算
print("\n4.3.3")
digits = list(range(1,10))
#   min()最小值
print(min(digits))
#   max()最大值
print(max(digits))
#   sum()总和
print(sum(digits))



#   4.3.4列表解析
print("\n4.3.4")
#   列表解析将for循环和创建新元素的代码合并到一行，并自动附加新元素
power = [value_3**2 for value_3 in range(11,21)]
print(power)

power_1 = [value_4**2 for value_4 in range(21,31)]
print(power_1)

power = [v**2 for v in range(31,41)]
print(power)
