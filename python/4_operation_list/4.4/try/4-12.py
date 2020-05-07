my_foods = ['pizza','falafel','carrot cake']
friends_foods = my_foods[:]
my_foods.append('meat')
friends_foods.append('beef')

print('My favorite three food are:')
for pisa in my_foods[0:3]:
    print(pisa)


print("\n")
print("My friend`s favorite three food are:")
for friend_food in friends_foods[0:-1]:
    print(friend_food)