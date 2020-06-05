# 8.4 传递列表

# 将列表传递给一个函数
def good_users(names):                         #  |   函数定义与形参
    """向列表中每位用户都发出简单的问候"""         # | 这是文档字符串
    for name in names:  # 函数遍历收到的列表        |
        msg = "Hello, " + name + "."             #|
        print(msg)                               #|   这些是函数体
    
username = ['han','tian','guo']   #定义一个用户列表
good_users(username) #                            |函数调用只是单纯的调用这个函数，执行这个函数的代码，传递函数完成工作所需的信息——实参










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



print("\n函数")

def print_models(need_models,done_models): # 定义了函数，包含两个形参   
    while need_models: # 循环这个形参的数据
        # 输出已打印的信息
        save = need_models.pop() # 模拟打印每个设计的过程
        print("The completed have: " + save)

        # 打印完存储在打印完列表
        done_models.append(save)   #将打印完所存储的变量加入到已完成列表

def show_done_models(done_models): # 定义函数，这是已打印完的数据所保存的形参
    """
    显示打印完的设计
    """
    print("the done is ")
    for n in done_models:
        print(n)  # 显示打印出来的每个模型的名称


a = ['iphone','xiaomi','huawei']   # 未打印的设计列表，也可以从用户那里获取
b = [] # 空列表

print_models(a,b)#调用函数（print_models）,并向它传递两个列表
show_done_models(b) # 调用函数，调用函数，并将打印好的列表传递给它
# 这两个有先后顺序，如果不先执行函数print_models,那么b就没有数据，所以函数show_done_models函数也获取不到打印完的数据
















# 8.4.2  禁止函数修改列表
print("\n8.4.2")
# 有时候需要禁止修改列表，可以向函数（形参）传递副本而不是原件，这样函数所作的任何修改都只影响副本，而丝毫不影响原件,如何传递副本呢，可以使用[:],切片法
# 已上面举例，不想清空a列表可以这样调用a
# print_models(a[:],b)
    



