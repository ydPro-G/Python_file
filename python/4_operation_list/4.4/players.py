#   4.4使用列表的一部分(处理列表的部分元素)

print("4.1.1")
#   4.4.1切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
#   切片：指定要使用的第一个元素和最后一个元素的索引(前三个元素)
print(players[0:3])
#   第二个到第四个元素
print(players[1:4])
#   没有指定第一个索引，python从列表开头开始提取(-1表示从位置0到位置-1之前的数，即-1不计算在内
print(players[:-1])
#   没有指定最后一个索引，python冲第一个索引开始提取，到列表末尾的所有元素。
print(players[0:])
#   负数索引返回离列表末尾相应距离的元素，因此可以指定第一个元素为负数索引，第二个元素为空，这样就可以随意输出最后几名的元素（最后4名
print(players[-4:])
print(players[:-1])

print("\n4.4.2")
#   4.4.2遍历切片
players_2 = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
#   要遍历列表中的部分元素，可在for循环中使用切片
for player in players_2[0:3]:
    print(player.title())


print("\n4.4.3")
#   复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
#   复制列表：创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引[:]
friend_foods = my_foods[:]
#   输出第一个列表
print("My favorite foods are:")
print(my_foods)
#   输出复制的列表
print("\nMy friend`s favorite foods are:")
print(friend_foods)
#   确定有两个列表
print("\n")
my_foods.append('kendeji')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)


players = ['charles', 'martina', 'michael', 'florence', 'eli']
for plpay in players[0:3]:
    print(plpay)
aa = players[:]
print(aa)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
for p in players[1:3]:
    print(p)
    