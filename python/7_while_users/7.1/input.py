# 7.1函数input()的工作原理:让程序暂停运行，等待用户输入，获取输入后，python将其储存在一个变量中
# 程序等待用户输入，在用户按回车键后继续运行，再将输入储存在变量中
# 针对集合中的每个元素都一个代码块
print("7.1")
message = input("Tell me someting, and I will repeat it back to you:")
print(message)



# input（）,Python将用户输入解读为字符串


#7.1.1 编写清晰的程序
print("\n7.1.1")
name = input("Please enter your name: ")
print("Hello " + name + " !")

# 超过一行的提示怎么编写？
# 将提示储存在一个变量中，再将该变量传递给另一个变量使用函数input（）
prompt = ("If you tell us who you are,we can presonalize the messages you see.")
prompt += "\nWhat is your first name? "  # 创建多行字符串的方法（运算符+=在存储在prompt中的字符串末尾附加一个字符串）

name = input(prompt)
print("\nHello, " + name + " !")



# 7.1.2  使用int()来获取数值的输入
print("\n 7.1.2")
age = input("How old are you? ")
age = int(age) # 将字符串转换成数值显示
if age >= 18:
    print("true")

print("\n") # 在实际程序中使用函数int()
height = input("How tall are you, in inches? ")
height = int(height) # 将字符串转换成数值显示

if height >=36:
    print("\nYou`re tall enough to ride!")
else:
    print("\nYou`ll be able to ride when you`re a little older.")




print("\n7.1.3")
# 7.1.3 求模运算符  
# 处理数值信息，求模运算符(%)是一个很有用的工具，将两个数相除并返回余数。
print(4 % 3) #  1 只指出余数是多少
print(5 % 3) #  2
print(6 % 3) #  0 一个数可被另一个数整除，余数就为0
print(7 % 3) #  1

print("\n")
# 判断一个数是奇数还是偶数
number = input("Enter a number,and I`ll tell you if it`s even or odd: ")
number = int(number) # 输入的数字以字符串显示，使用int()将字符串转换成数值显示

if number % 2 == 0: # 如果求模2后是0，说明是整数
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")





a = "tell me? "
message = input(a)
print(message)