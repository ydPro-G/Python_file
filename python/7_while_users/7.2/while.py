# 7.2 while循环不断运行

# 7.2.1 使用while循环
print("7.2.1")
current_number = 1
while current_number <= 5:  # 只要变量小于或等于5，就接着运行这个循环。循环中的代码打印current_number的值
    print(current_number)
    current_number += 1 #(current_number = current_number + 1的缩写)，将其值加1





# 7.2.2 让用户选择何时退出
print("\n7.2.2")
prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program." # 定义一条提示消息：输入信息或者输入quit退出
message = "" # 创建一个变量，储存用户输入的值
while message != 'quit': #首次执行while语句时，需要将message的值与quit进行比较
    message = input(prompt) # 显示提示消息，并等待用户输入，获取用户输入的值，储存在message中
    print(message)


# 修改美中不足
print("\n加if判断")
