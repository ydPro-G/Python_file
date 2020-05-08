#   6.1简单的字典
print("6.1")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])


#   6.2使用字典
#   字典是一系列（键-值）对，每个键都与一个值相关联，可以使用键来访问相关联的值，值可以是任何python对象（数字，字符串，列表，字典）、
#   字典用放在花括号{}中的一系列（键-值）对表示,(键-值)对是两个相关联的值，指定键时，python将返回与之相关联的值
#   键和值之间用冒号分隔，不同键之间用逗号分隔
print("\n6.2")
alien_0 = {'color': 'green'}
print(alien_0['color'])


#   6.2.1访问字典中的值
#   依次指定字典名，放在方括号内的键
print("\n6.2.1")
alien_0 = {'color': 'red'}
print(alien_0['color'])

alien_0 = {'color': 'green', 'points': 5}
#   从字典获取与键'points'相关联的值，将这个值储存在变量new_points中
#   把整数转换为字符串str（）
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")


#   6.2.2添加键-值对
#   字典是动态结构，可随时添加键-值对
#   添加：依次指定字典名，键，值
print("\n6.2.2")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

#   添加x坐标为0，y坐标为25
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


#   6.2.3先创建一个空字典
#   1.用户提供的数据2.自动生成大量键-值对的代码
print('\n6.2.3')
alien_0 = {}
alien_0['points'] = 5
alien_0['color'] = 'yellow'
print(alien_0['color'])



#   6.2.4修改字典中的值———依次指定——字典名-方括号——键——等号——值
print("\n6.2.4")
alien_0 = {'color': 'green'}
print("The alien color is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien color now is " + alien_0['color'] + ".")


print("\n")
# 外星人原始位置（x,y），外星人速度
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed']  == 'slow':
    x_increment = 1
elif alien_0['speed']  == 'medium':
    x_increment = 2
    # 这个外星人的速度一定很快
else:
    x_increment = 3

# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']) + ".")







# 6.2.5  删除键-值对
# del语句彻底删除
print("\n6.2.5")
alien_0 = {'color': 'green','points': 5}

del alien_0['points']
print(alien_0)








# 6.2.6  由类似对象组成的字典
print("\n6.2.6") 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah`s favorite language is " + 
    favorite_languages['sarah'].title() + 
    ".")
    