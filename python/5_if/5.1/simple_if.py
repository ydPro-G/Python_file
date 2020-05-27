#   5.1简单示例
print("5.1")
cars = ['audi', 'bmw', 'subaru', 'toyota']

#   都应首字母大写打印，但，bmw全大写打印(大写：upper，小写：lower)
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


#   5.2条件测试
print("\n5.2")
#   5.2.1检测是否相等：一个等号是陈述（将变量X的值设置为xx），两个等号是发问（变量X的值是xx吗？），相等返回True,不相等返回False

#   5.2.2 大小写对比
#   函数.lower()可用来检查变量的值，对大小写不同的值同时进行小写比较，不会影响原来的变量
car = 'Audi'
car.lower() == 'audi'  #将变量里的元素转换为小写比较
print(car)

#   5.2.3检查是否不相等
print("\n5.2.3")
requested_topping = 'mushrooms'
#   !=比较requested_topping的值和anchovies的值是否不相等，如果不相等返回True，并执行下面的语句，如果相等返回False，不执行下面的语句
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#   5.2.4比较数字
print("\n5.2.4")
#   检查数值

answer = 17
if answer != 42:
    print("That is not the corret answer. Pkease try again!")

#   5.2.5检查多个条件
print("\n5.2.5")

#   使用 and 检查多个条件:多个条件都为Ture,整个表达式都为Ture.如果至少有一个测试没通过，整个表达式为False
#   改善可读性(age_0 >= 21) and (age_1 >= 21)
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
print("Flase")

age_1 = 22
age_0 >= 21 and age_1 >= 21
print("Ture")

#   使用 or 检查多个条件,只要有至少一个条件满足，就能通过整个测试。测试都没有通过时，使用or表达式才为False
age_0 = 22
age_1 = 18 
age_0 >= 21 or age_1 >= 21
print("Ture")

age_0 = 18
age_0 >=21 or age_1 >=21
print("False")

#   5.2.6检查特定值是否包含在列表中
print("\n5.2.6")
#   判断特定的值是否已包含在列表中，可使用关键词in
requested_toppings = ['mushromms','onions','pineapple']
'mushromms' in requested_toppings
print("True")

'pepperoni' in requested_toppings
print("False")

#   5.2.7检查特定值是否不包含在列表中
print("\n5.2.7")
#   判断特定的值未包含在列表中，可使用关键词not in
banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

#   5.2.8布尔表达式

