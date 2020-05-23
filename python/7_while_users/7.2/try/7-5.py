age = "How old are you? "
message = input(age)
message = int(message)

if message < 3:
    print("free!")
elif message < 12:
    print("10 dollars!")
else:
    print(("15 dollars!"))