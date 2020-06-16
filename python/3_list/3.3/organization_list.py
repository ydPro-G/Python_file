#    3.3.1使用方法sort()对列表进行永久性排序
#    sort()方法永久性改变了列表元素的排列顺序，按照字母顺序排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#    向sort()方法传递参数reverse=True 让列表元素按与字母顺序相反的顺序排列列表元素,对列表元素排序修改是永久性的。
cars.sort(reverse=True)
print(cars)


#    3.3.2使用函数sorted()对列表进行临时排序
#    按照原始顺序打印列表
print("Here is the original list:")
print(cars)
#    使用函数sorted()对列表按照字母顺序进行临时排序
print("\nHere is the sorted list:")
print(sorted(cars))
#    按字母顺序相反的顺序显示列表进行临时排序，使用sorted.(,reverse=True)函数
print("\nHere is the sorted(reverse=True) list:")
print(sorted(cars, reverse=True))


#    3.3.3 倒着打印列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

#    使用方法reverse()倒着打印列表，永久性修改列表元素的排列顺序
cars.reverse()
print(cars)
#    对列表再次调用reverse()将列表元素恢复到原来的排列顺序，
cars.reverse()
print(cars)



#    3.3.4确定列表长度
#    len()方法返回对象（字符，列表，元组等）长度，项目个数
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
