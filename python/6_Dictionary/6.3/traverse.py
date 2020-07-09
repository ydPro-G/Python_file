# 6.3  遍历列表
# 6.3.1  遍历所有的键-值 对
print("6.3.1")
user_0 = {
    'username': 'efeimi',
    'first': 'enrico',
    'last': 'fermi',
}
# 第一部分：声明两个变量，用于储存键，值。
# 第二部分：包含字典名和方法items()，它返回一个键值对列表
# for循环依次将每个键-值对储存到指定的两个变量中
for key,value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'ruby',
    'phil': 'python',
}
print("\n")
for name,language in favorite_language.items():
    print(name.title() + "`s favorite language is " + 
    language.title() + ".")









# 6.3.2  遍历字典中的所有 键
# 使用方法.keys()提取字典中的所有键，将它们依次储存到变量中
print("\n6.3.2")
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# 使用方法.keys()提取字典favorite_language中的所有键，将它们依次储存到变量中
for name in favorite_language.keys():
    print(name.title())

#  使用当前键来访问与之相关联的值
print("\n")
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friend = ['phil','sarah'] # 创建列表指出朋友
for name in favorite_language.keys(): # 使用方法.keys提取字典中所有键并储存到变量中
    if name in friend: 
        print(" Hi " + name.title() + 
        ", I see your favarite language is " +
        favorite_language[name].title() + ".") # 将变量name的当前值作为键

# 使用keys()确定某人是否接受了调查
print("\n")
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
if 'erin' not in favorite_language.keys():
    print("Erin,please take our poll!")






# 6.3.3  按   顺序   遍历字典中的所有键
# 获取字典的元素时，获取顺序时不可预测的。
# 以特定的顺序返回元素，在for循环中对返回的键进行排序，使用函数sorted()
print("\n6.3.3")
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# 对方法dictionary.keys()结果     调用函数sorted()
# 在遍历前对这个列表进行排序
for name in sorted(favorite_language.keys()): 
    print(name.title() + ", thank you for taking the poll.")






# 6.3.4  遍历字典中得分所有   值
# 使用方法values(),返回一个值的列表，而不包含任何键
print("\n6.3.4")

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for language in favorite_language.values():
    print(language.title())

# 剔除重复项，使用   集合set(a)
print("\n")
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for language in set(favorite_language.values()): # 对包含重复元素的列表调用set()，剔除重复元素
    print(language.title())

