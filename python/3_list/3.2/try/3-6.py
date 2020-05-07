#    邀请嘉宾前来赴宴——基础数据
guest = ['A', 'B', 'C', 'D', 'E', 'F']
#    添加一条print函数，说明找到了一个更大的餐桌
print("Hi!everyone,I found a bigger table.")
#    使用insert()方法将一位新嘉宾添加到名单开头
guest.insert(0, "Z")
#    使用insert()方法将一位新嘉宾添加到名单中间
guest.insert(3, "X")
#    使用append()方法将一位新嘉宾添加到名单末尾
guest.append("G")
#    打印一系列消息，向名单中的每位嘉宾发出邀请
A_guest = "I hope you can come for dinner " + guest[0] + "."
B_guest = "I hope you can come for dinner " + guest[1] + "."
C_guest = "I hope you can come for dinner " + guest[2] + "."
D_guest = "I hope you can come for dinner " + guest[3] + "."
E_guest = "I hope you can come for dinner " + guest[4] + "."
F_guest = "I hope you can come for dinner " + guest[5] + "."
Z_guest = "I hope you can come for dinner " + guest[6] + "."
X_guest = "I hope you can come for dinner " + guest[7] + "."
G_guest = "I hope you can come for dinner " + guest[8] + "."
print(A_guest, B_guest, C_guest, D_guest, E_guest,
      F_guest, Z_guest, X_guest, G_guest, sep="\n")
