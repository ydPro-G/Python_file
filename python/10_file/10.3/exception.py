# 10.3 异常
# 异常：特殊对象
# 如果编写了处理该异常的代码，程序将继续运行
# 异常使用try-except代码块处理





print("10.3.1-2")
# 10.3.1-2  处理ZeroDivisionError异常

# 不能将一个数字除以0

# 用try - except代码块来自定义错误提示

# 如果try代码块中代码没错，Python将跳过except代码块，如果错了，Python将执行except
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("不能除以0")








# 10.3.3 使用异常避免崩溃

# print("Give me two numbers, and I`ll divide them.")
# print("Enter 'q' to quit.")

# try:
#     while True:
#         first_number = input("\nfirst number is: ")
#         if first_number == 'q':
#             break
#         second_number = input('Second number:')
#         if second_number == 'q':
#             break
#         answer = int(first_number) / int(second_number)
#         print(answer)
# except ZeroDivisionError:
#     print("不能除以0")  # 不能让用户看见traceback，也会暴漏系统安全性









# 10.3.4 else代码块

print("Give me two numbers, and I`ll divide them.")
print("Enter 'q' to quit.")


while True:
    first_number = input("\nfirst number is: ")
    if first_number == 'q':
        break
    second_number = input('Second number:')
    if second_number == 'q':
        break

    # python尝试执行try代码块中的代码，只有可能引发异常的代码才放在try语句中
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError: # 出现异常时输出数据
        print("相除不能为0！")

    # 仅在try代码块成功执行时才需要运行的代码，这些代码放在else代码块中
    else: 
        print(answer)   
        

        



