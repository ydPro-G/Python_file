#   使用函数.lower()来检查变量的值，进行小写比较，不会更改变量的值
food = 'Beef'
print(food.lower() == 'beef')


#   检查两个数字是否相等，大于，小于，大于等于，小于等于
age = 20
print(age == 20)
print(age > 20)
print(age >= 20)
print(age < 20)
print(age <=20 )

print("\n")
age_1 = 18
age_2 = 22
print(age_1 >=18 and age_2 >=23)
print(age_1 ==18 and age_2 <=23)

print('\n')
print(age_1 ==12 or age_2 >=18)
print(age_1 == 12 or age_2 >=23)

#   特定值是否包含在列表中
print("\n")
foods = ['apple','banana','pizza']
print('pizza' in foods)
print('beef' in foods)

#   特定值是否未包含在列表中
print('\n')
print('pizza' not in foods)
print('beef' not in foods)