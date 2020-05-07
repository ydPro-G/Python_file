number = [value for value in range(1,1000001)]
#    让python从列表中取出一个数字，并将其储存在临时变量value中，再让python打印储存在列表中的数字，循环
for value in number:
    print(value)

number = []
#    新建一个临时变量，将临时变量储存在列表中，循环输出这个变量,而循环输出这些列表则，一次输出一个列表+1
for value in range(1,1000001):
    number.append(value)
    print(number)



