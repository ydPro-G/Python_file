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
show_done_models(b) # 调用函数，并将打印好的列表传递给它
