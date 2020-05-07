#   5.3.1简单的if语句  
print("5.3.1")
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have registered to vote yet?")


#   5.3.2if-else语句
print("\n5.3.2 if-else")
age = 17
#   通过条件测试执行if语句，未通过执行else语句
if age >= 18:
    print("You are old enough to vote!")
    print("Have registered to vote yet?")
else:
    print("Sorry,you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


#   5.3.3if-elif-else结构   python只执行其中的一个代码块，条件测试通过后，执行紧跟在它后面的代码，并跳过余下的测试。

print("\n简洁版")
age_1 = 18

if age_1 < 4:
    price = 0
elif age_1 < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")


#   5.3.4使用多个elif代码块
print("\n5.3.4")
age_2 = 17
if age_2 < 4:
    price_2 = 0
elif age_2 < 18:
    price_2 = 5
elif age_2 < 65:
    price_2 = 10
else:
    price_2 = 5

print("Your admission cost is $" + str(price_2) + ".")



#   5.3.5 省略else代码块
#   只要不满足if或elif中的条件测试，else中的代码就会执行，这可能会引入无效甚至恶意的数据
print("\n5.3.5")
age_3 = 65
if age_3 < 4:
    price_3 = 0
elif age_3 < 18:
    price_3 = 5
elif age_3 < 65:
    price_3 = 10
elif age_3 >= 65:
    price_3 = 5

print("Your admission cost is $" + str(price_3) + ".")


#   5.3.6测试多个条件  有时候必须检查关心的所有条件，在这种情况下应使用一系列不包含elif和else代码块的简单if语句
print("\n5.3.6")
requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'peperoni' in requested_toppings:
    print("Adding mushrooms.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza!")




