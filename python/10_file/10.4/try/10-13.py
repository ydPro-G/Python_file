

import json

def get_stored_username(): # 存储了用户名这个函数就获取并返回它
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)  # 使用json.load()来加载存储在json文件中的信息
    except FileNotFoundError:  # 值不存在返回None
        return None
    else:
        return username # 值存在返回变量



 # 这个函数获取用户输入，然后获取输入的变量被写入转储到json文件中，最后返回获取用户输入的变量
def get_new_username():
    """提示用户输入名字"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username




 # 定义两个变量，每一个变量都获取一个函数，输出相应的内容
def greet_user():
    """问候用户，指出用户名字"""
    username = get_stored_username()
    filename = 'username.json'
    if username:
        print(username)
        ask = input('Your user name is ' + username + 'right(y/n)?')
        if ask == 'y':
            print('welcome,' + username)
        else:
            username = get_new_username()
            print(('We`ll remember you when you come back, ' + username + '.'))


greet_user()
