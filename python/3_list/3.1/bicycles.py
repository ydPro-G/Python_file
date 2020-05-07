#  3.1 列表，可以包含字母表中的所有字母数字0-9，通常给列表指定一个附属的名称
#      用[]来表示列表，用逗号分隔其中的元素。
bicycles = ['trek','cannoandle','redline','specialized']

#  3.1.1 要访问列表元素可指出列表的名称，再指出元素的索引
print(bicycles[0]) 

#  可使用方法来让元素更整洁 
print(bicycles[1].title())

#  3.1.2 索引从0开始,将索引指定为-1，可让python返回最后一个列表元素
print(bicycles[2])
print(bicycles[-1])


# 3.1.3  使用列表中的各个值 
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)