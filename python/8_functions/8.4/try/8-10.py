# 在函数中修改列表

def show_magicians(names,great):
    """
    打印魔术师的名字
    """
    while names:  # 注意使用while，不然只会弹出和输出一个元素
        save = names.pop()
        print(save)
        great.append(save)


def make_great(great):
    for nice in great:
        print("The great" + nice)


magician_names = ['大卫','哈利波特']
b = []

show_magicians(magician_names,b)
make_great(b)







