#    邀请嘉宾前来赴宴——基础数据
guest = ['A', 'B', 'C', 'D', 'E', 'F']
A_guest = "I hope you can come for dinner " + guest[0] + "."
B_guest = "I hope you can come for dinner " + guest[1] + "."
C_guest = "I hope you can come for dinner " + guest[2] + "."
D_guest = "I hope you can come for dinner " + guest[3] + "."
E_guest = "I hope you can come for dinner " + guest[4] + "."
F_guest = "I hope you can come for dinner " + guest[5] + "."
print(A_guest, B_guest, C_guest, D_guest, E_guest, F_guest, sep='\n')
#    使用.pop()指出A嘉宾无法来赴宴
poped_guest = guest.pop(0)
print(poped_guest + " can not come here.")
#    将无法赴宴的嘉宾姓名替换为新的嘉宾的名字
guest.insert(0, "G")
#    再次打印消息，向名单中的每位嘉宾发出邀请
G_guest = "I hope you can come for dinner " + guest[0] + "."
print(G_guest, B_guest, C_guest, D_guest, E_guest, F_guest, sep='\n')

