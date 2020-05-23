







pizza = "Please enter pizza toppings. "
pizza += "\nif you type 'quit',you exit:"

message = ""
while message != 'quit':
    message = input(pizza)
    if message != 'quit':
        print(message)













pizza = "Please enter pizza toppings. "
pizza += "\nif you type 'quit',you exit:"

message = True
while message:
    message = input(pizza)
    if message == 'quit':
        message = False
    else:
        print(message)
        