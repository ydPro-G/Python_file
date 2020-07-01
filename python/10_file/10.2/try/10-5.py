filename = 'cause.txt'

with open(filename,'a',encoding='utf-8') as file_object:
    while True:  # 编写一个while循环
        message = input('为什么喜欢编程：')
        if message == 'q':
            break
        else:
            file_object.write(message + '\n') # 可以和print一样用