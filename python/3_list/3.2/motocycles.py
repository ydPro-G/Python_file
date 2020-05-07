#  3.2 随着程序的运行增删元素

#  3.2.1 修改列表元素
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
#    修改列表motocycles第一个元素
motorcycles[0] = "ducati"
print(motorcycles)

#  3.2.2 在列表中添加元素
#   1在列表末尾添加元素
#    使用方法append()将元素添加到列表末尾，不影响列表中其他元素
motorcycles.append('halei')
print(motorcycles)
#  实际运用 先创建空列表，将用户提供的每个新值附加到列表中
names = []
names.append('z')
names.append('q')
names.append('s')
print(names)
#   2在列表中插入元素
#     使用方法insert()可在列表中任意位置添加新元素，需指定新元素的索引和值
motorcycles.insert(0, 'xiaomoto')
print(motorcycles)

#  3.2.3 从列表中删除元素
#    1.使用del语句删除元素，知道其索引可删除任何位置的列表元素
del motorcycles[0]
print(motorcycles)
#    2.使用方法pop()删除元素
#    使用.pop（）方法将motocycles的值弹出到poped_motocycles中，并依然能够访问
popped_motocycles = motorcycles.pop()
print(motorcycles)
print(popped_motocycles)

last_owned = motorcycles.pop()
print("The last motocycle I owned was a " + last_owned.title() + ".")
#    3.使用.pop()方法弹出列表中任何位置处的列表，只需在阔海中指定要删除元素的索引即可
frist_owned = motorcycles.pop(1)
message = "The frist motocycle I owned was a " + frist_owned.title() + "."
print(message)  # 提示：使用pop()方法弹出的元素就不在列表中了。如果不再使用，用del，如果继续使用用pop()
motorcycles.append('pangbadi')
motorcycles.append('baoma')
motorcycles.insert(1, 'xiaofeiji')
print(motorcycles)
#    4.根据值删除元素
#    删除ducati
motorcycles.remove('ducati')
print(motorcycles)
# 使用remove（）从列表中删除元素时，也可以接着使用被删除元素的值
too_expensive = 'baoma'
motorcycles.remove(too_expensive)
message_remove = "\nA " + too_expensive.title() + " is too expensive for me."
print(message_remove)
print(motorcycles)