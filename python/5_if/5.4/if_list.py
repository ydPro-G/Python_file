#   5.4.1 使用if检查特殊元素
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

print("\n 加if判断")
requested_toppings = ['mushrooms','green peppers','extra cheese']
#   让python从列表中取出一个元素，将其储存在临时变量中，接下来循环这个操作，直到列表中没有其他值
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry,we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("Finshed making your pizza!")

#   5.4.2 在if语句中将列表名用在条件表达式中时，Python将在列表至少包含一个元素时返回True，并在列表为空时返回False
print("\n5.4.2")
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinisted making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


#   5.4.3使用多个列表
print("\n5.4.3")
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry,we don`t have" + requested_topping + ".")