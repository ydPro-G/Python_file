# 6.4  嵌套，在列表中嵌套字典，在字典中嵌套列表，在字典中嵌套字典

# 6.4.1 字典列表 将字典嵌套进列表，使用for循环输出列表内容
alien_0 = {'color': 'green', 'point': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
print("\n")
# 使用range()生成30个外星人

# 创建一个用于储存外星人的空列表
aliens = []

# 创建30个绿色外星人
for alien_number in range(30):  #告诉python我们要重复这个循环多少次
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien) # 每次执行这个循环都创建一个外星人，将其附加到aliens末尾

# 显示前五个外星人
for alien in aliens[:5]: # 使用一个切片打印前五个外星人
    print(alien)

# 显示创建了多少外星人
print("Total number of aliens: " + str(len(aliens)) + ".")

print("\n")

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'solw'}
    aliens.append(new_alien)

for alien in aliens[0:3]: 
    # 编写一条if语句来确保只修改绿色外星人，如果是绿色，将其颜色，速度，点数修改
    if alien['color'] == 'green':  #注意是alien
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien) 

print("\n")

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'solw'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10 
        alien['speed'] = 'medium'
    elif alien == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien)