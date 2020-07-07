print('\n10.4.3')

# 10.4.3  重构 
 # 代码可以正常运行，但是可做进一步改进——将代码划分为一系列完成具体工作的函数。
 # 这样的过程被称为重构


 # 将大部分逻辑放到多个函数里,这样只需要调用函数就好




# 获取存储用户名

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
    if username:
        print("Welcome back " + username + "!")
    else:
        username = get_new_username()
        print("We`ll remember you when you come back, " + username + ".")


# 调用函数
greet_user() 