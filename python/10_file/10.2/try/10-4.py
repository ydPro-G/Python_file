filename = 'guest_book.txt'

with open(filename,'w',encoding='utf-8') as user_name:  # 在with语句用while循环
    while True:
        message = input('请输入你的名字：')
        if message == 'no':
            break
        else:
            user_name.write(message + '\n')

   
