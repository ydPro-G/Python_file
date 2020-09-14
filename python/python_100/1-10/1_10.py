# 1. 找到2000——3200之间可被7整除但不是5的倍数的所有数字，数字以逗号分隔打印在一行上：
for i in range(2000,3201):
    if i%7 == 0 and i%5 != 0:
        print(i,end=",")
print("\b")

# 一个能计算给定数字阶乘的程序，用逗号打印
num = int(input())

fact = 1
i = 1

if num < 0:
    print("抱歉，负数没有阶乘")
elif num == 0:
    print("0的阶乘为1")
else:
    for i in range(1,num + 1):
        fact = fact * i
    print("%d的阶乘为%d"%(num,fact))