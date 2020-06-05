
# 传递函数

def show_magicians(names):
    """
    打印魔术师的名字
    """
    for name in names:
        print(name)

magicians_names = ['大卫','哈利波特','皮平']

show_magicians(magicians_names)


# 两种方法

def show_magicians(names):
    """
    打印魔术师的名字
    """
    while names:
        save = names.pop()
        print(save)


magicians_names = ['大卫','哈利波特','皮平']

show_magicians(magicians_names)
