# 6.4  嵌套，在列表中嵌套字典，在字典中嵌套列表，在字典中嵌套字典

# 6.4.1 在列表中嵌套字典，使用for循环输出列表内容
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
for alien_number in range(30):  #其唯一的用途是告诉Python我们要重复这个循环多少次。每次执行这个循环时，都创建一个外星人
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
    # 编写一条if语句来确保只修改绿色外星人，如果是绿色，将其颜色，速度，点数修改
    if alien['color'] == 'green':  #注意是alien
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15   # if和elif的关系：python只执行其中一个代码块，通过条件测试后执行紧跟它后面的代码。跳过其余测试

for alien in aliens[:5]:
    print(alien)



# 6.4.2  在字典中储存列表
print("\n6.4.2")
# 储存所点披萨信息

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra cheese'],
}

# 描述所点披萨
print("You ordered a " + pizza ['crust'] + "-crust pizza" + 
    " with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)


# 多个喜欢的语言
print("\n")
favorite_languages = {
    'jen': ['Python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby','go'],
    'pjil': ['python','haskell'],
}

for name,languages in favorite_languages.items():
        print("\n" + name.title() + " favorite languages are:")
        for language in languages: # 在一个循环里面
                               # 使用变量来储存值，因为值是列表
            print("\t" + language.title())
   
