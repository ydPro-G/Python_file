print('这是一个加法运算器')
print('输入‘Q’退出')

while True:
    f_num = input('输入一个数字：')
    if f_num == 'Q':
        break

    l_num = input('请输入一个数字:')
    if l_num == 'Q':
        break
    
    try:
        num = int(f_num) + int(l_num)
    except ValueError:
        print('请输入数字！')

    else:
        print(num)