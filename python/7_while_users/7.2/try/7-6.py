
# 7-4
pizza = "Please enter pizza toppings. "
pizza += "\nif you type 'quit',you exit:"

message  = True
while message:
    message = input(pizza)
    if message == 'quit':
        message = False
    else:
        print(message)










# 7-5
age = "How old are you? "
age += "\nPlease enter:"

while True:
    message = input(age)
    message = int(message)
    if message < 3:
        print("0$")
    elif message < 12:
        print("10$")
    else:
        print("15$")
    break


