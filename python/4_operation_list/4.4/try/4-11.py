pizza = ['bishengke','maidanglao','lanniao']
friend_pizza = pizza[:]
pizza.append('jingongmen')
friend_pizza.append('xingbake')

print("My favorite pizzas are:")
for pisa in pizza:
    print(pisa)
print("\n")

print("My friend`s favorite pizzas are:")
for friend_pisa in friend_pizza:
    print(friend_pisa)
