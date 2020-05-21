# 7.2 while循环不断运行

# 7.2.1 使用while循环,让while循环不断地运行，直到指定的条件不满足为止。
print("7.2.1")
current_number = 1
while current_number <= 5:  # 只要变量小于或等于5，就接着运行这个循环。循环中的代码打印current_number的值
    print(current_number)
    current_number += 1 #(current_number = current_number + 1的缩写)，将其值加1





# 7.2.2 让用户选择何时退出
print("\n7.2.2")
prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program." # 定义一条提示消息：输入信息或者输入quit退出
message = "" # 创建一个空变量，储存用户输入的值，首次执行while语句时，需要将message的值与quit进行比较
while message != 'quit': # 不等与quit执行接下来的循环
    message = input(prompt) # 显示提示消息，并等待用户输入，获取用户输入的值，储存在message中
    print(message)  # 输出用户输入


# 修改美中不足
print("\n加if判断")
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit': # 在显示消息前做简单检测，如果不是quit打印message，是quit的话就不打印
        print(message)




# 7.2.3  使用标志  在要求很多条件都满足才继续运行的程序中，定义一个变量，判断整个程序是否处于活动状态
print("\n7.2.3")

# 使用一个标志指出程序是否处于活动状态，如果要添加测试（elif）以检查是否发生了其他导致变量Flase的事件，将很容易。

prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."

active = True # 定义变量，程序处于活动状态（简化了while语句，不需要做任何比较）
              # 只要变量为true，循环就将继续
while active:
    message = input(prompt)

    if message == 'quit':  # 使用if语句检查变量message的值，如果输入是quit
        active = False # 用户输入quit时，，将变量设置为False，导致while不循环
    else:
        print(message)





# 7.2.4  使用break退出循环
print("\n")
prompt = "Please enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I`d love to go to " + city.title() + ".")



