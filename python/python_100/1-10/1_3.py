# 1. 找到2000——3200之间可被7整除但不是5的倍数的所有数字，数字以逗号分隔打印在一行上：
for i in range(2000,3201):
    if i%7 == 0 and i%5 != 0:
        print(i,end=",")
print("\b")

# 2一个能计算给定数字阶乘的程序，用逗号打印
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

# 3.给定的整数n，编写一个程序生成字典，包括(i,ixi)这样的证书然后输出
n = int(input('请输入一个数字:'))
ans = {i : i*i for i in range(1,n*1)}
print(ans)

