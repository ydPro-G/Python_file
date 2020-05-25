sandwich_orders = ['sandwich1','sandwich2','sandwich3','sandwich4']
finished_sandwiches = []

while sandwich_orders:
    finished = sandwich_orders.pop()

    print("I made your " + finished + " sandwich.")

    finished_sandwiches.append(finished)
print("\nSandwich list: ")
for f in finished_sandwiches:
    print(f)