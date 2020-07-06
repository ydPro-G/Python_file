print('这是一个加法运算')
print('输入‘Q’退出')

while True:
    first_number = input('请输入一个数字：')
    if first_number == 'Q':
        break

    last_number = input('请输入一个数字：')
    if last_number == 'Q':
        break

    try:
        number = int(first_number) + int(last_number)
    except ValueError:
        print('请输入数字！')

    else:
        print(number)
        

    
    
        
    
        

    
