# 8.4 传递列表

# 将列表传递给一个函数
def good_users(names):                         #  |   函数定义与形参
    """向列表中每位用户都发出简单的问候"""         # | 这是文档字符串
    for name in names:  # 函数遍历收到的列表        |
        msg = "Hello, " + name + "."             #|
        print(msg)                               #|   这些是函数体
    
username = ['han','tian','guo']   #定义一个用户列表
good_users(username) #                            | 这是函数调用    调用函数，并将这个列表传递给它










#  8.4.1 在函数中修改列表
# 将列表传递给函数后，函数就可对其进行修改
# 在函数中对这个列表做的任何修改都是永久性的
print("\n8.4.1")


# 创建一个列表,打印前存储
unprinted_designs = ['iphone','huawei','xiaomi']
# 打印后存储
completed_models = []

# 打印后从unprinted列表中转移到completed列表中
while unprinted_designs:
    storage = unprinted_designs.pop()
    completed_models.append(storage)

print("The printed ones are:")
for completed_model in completed_models:
    print(completed_model)


# 重新组织这些代码，编写两个函数，每个函数都做一件具体的工作
# 第一个