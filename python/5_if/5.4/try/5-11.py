#   序数表示位置，如1st和2nd。大多数序数都以th结尾，只有1、2和3例外。
#在一个列表中存储数字1~9。
#遍历这个列表。
#在循环中使用一个if-elif-else 结构，以打印每个数字对应的序数。
#输出内容应为1st 、2nd 、3rd 、4th 、5th 、6th 、7th 、8th 和9th ，但每个序数都独占一行。
numbers = list(range(1,10))   #   list为数字列表
for number in numbers:
    number = str(number)   #使用str（）函数将数字列表变为字符
    if number == '1':
        print(number + "st")
    elif number == '2':
        print(number + "nd")
    elif number == '3':
        print(number + "rd")
    else:
        print(number + "th")
        