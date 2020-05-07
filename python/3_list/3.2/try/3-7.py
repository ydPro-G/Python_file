#    邀请嘉宾前来赴宴——基础数据
guest = ['A', 'B', 'C', 'D', 'E', 'F']
#    添加一条print函数，说明找到了一个更大的餐桌
#    使用insert()方法将一位新嘉宾添加到名单开头
guest.insert(0, "Z")
#    使用insert()方法将一位新嘉宾添加到名单中间
guest.insert(3, "X")
#    使用append()方法将一位新嘉宾添加到名单末尾
guest.append("G")
#    打印一系列消息，向名单中的每位嘉宾发出邀请
#    只能邀请两名嘉宾
print("I am sorry,We can only invite two guests.")
poped_A = guest.pop(1)
print("I am sorry " + poped_A + " can`t have dinner with you.")
poped_B = guest.pop(1)
print("I am sorry " + poped_B + " can`t have dinner with you.")
poped_C = guest.pop(2)
print("I am sorry " + poped_C + " can`t have dinner with you.")
poped_D = guest.pop(2)
print("I am sorry " + poped_D + " can`t have dinner with you.")
poped_E = guest.pop(2)
print("I am sorry " + poped_E + " can`t have dinner with you.")
poped_F = guest.pop(2)
print("I am sorry " + poped_F + " can`t have dinner with you.")
poped_G = guest.pop(2)
print("I am sorry " + poped_G + " can`t have dinner with you.")
z_guest = guest[0]
print("I hope you can come for dinner " + z_guest + ".")
x_guest = guest[1]
print("I hope you can come for dinner " + x_guest + ".")
del guest[0]
del guest[0]
print(guest)

