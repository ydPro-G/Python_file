# 在函数中修改列表副本副本，不修改列表

def show_magicians(names,great):
    """
    打印魔术师的名字
    """
    while names:  # 注意使用while，不然只会弹出和输出一个元素
        save = names.pop()
        print(save)
        great.append(save)
    great_two = great[:]
    return great_two


def make_great(great_two):
    
    for nice in great_two:
        print("The great: " + nice)


magician_names = ['大卫','哈利波特']
b = []

show_magicians(magician_names,b)
make_great(b)






def make_great(magicians,new_magicians): #对列表修改的函数
 while magicians:
   current_magician = magicians.pop() #删除原列表中的元素
   current_magician = "The Great " + current_magician
   new_magicians.append(current_magician)

def show_magicians(new_magicians):
 for magician in new_magicians:
  #便利所有的magicians中的元素
  print(magician) 

magicians = ['fake','ppd','moon']
new_magicians = []

make_great(magicians[:],new_magicians)#调用函数make_great 传递magicians[]副表magicians[:]
show_magicians(new_magicians)#输出新表
show_magicians(magicians)#输入原表




