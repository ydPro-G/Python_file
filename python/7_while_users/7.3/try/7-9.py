sandwich_orders = ['pastrami','sandwich1','pastrami','sandwich2','pastrami','sandwich3']
finished_sandwiches = []

while sandwich_orders:
    finished = sandwich_orders.pop()

    print("I made your " + finished + " sandwich.")

    finished_sandwiches.append(finished)


print("pastrami is 0.")
while 'pastrami' in finished_sandwiches:
    finished_sandwiches.remove("pastrami")# while循环删除列表中的包含特定值的所有的列表元素


print("\nSandwich list: ")
for f in finished_sandwiches:
    print(f)