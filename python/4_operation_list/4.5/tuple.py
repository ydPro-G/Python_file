#   4.5.元组
print("4.5.1")
#   不可修改的值称为不可变的，不可变的列表被称为元组
#   使用圆括号来标识，使用索引来访问其元素
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#   试图修改元组的操作是被禁止的


#   4.5.2遍历元组中所有值
print("\n4.5.2")
dimensions = (200, 50)
#   与列表一样，可以使用for循环来遍历元组中的所有值
for dimension in dimensions:
    print(dimension)


#   4.5.3修改元组变量
print("\n4.5.3")
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)