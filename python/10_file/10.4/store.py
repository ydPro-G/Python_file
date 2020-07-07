# 10.4 存储数据

 # 存储用户输入的信息
 # 使用模块json来存储数据
 # 模块json将python数据结构转储到文件中
 # 还可以使用json在程序之间分享数据







print('10.4.1')
 # 10.4.1 使用json.dump()和json.load()

  # 使用json.dump()来存储这组数字  （转储）
  # 使用json.load()来读取这组数字  （负载）

   # json.dump()接受两个实参，要存储的数据以及可用于存储数据的文件对象

 # 导入模块json
import json

 # 创建一个数字列表
numbers = [2,3,5,7,11,13]

 # 指定数字列表要存储的文件名
filename = 'numbers.json'

 # 以写入模式 打开 文件
with open(filename,'w') as f_obj:
    # 使用json.dump()将数字列表转储到json中；两个实参，要存储的数据和存储数据的文件对象
    json.dump(numbers,f_obj)



 # 读取的时前面写入的文件 
filename_load = 'numbers.json'

 # 打开这个文件
with open(filename) as f_load:
    # 使用函数json.load()加载存储在json文件中的信息，并存储到变量中
    numbers_load = json.load(f_load)

print(numbers_load)










print('\n10.4.2')
# 10.4.2 保存和读取用户生成的数据
 #  保存用户生成的数据


import json
 # 将用户输入存储到变量中
username = input('What is your name? ')
 # 指定文件
filenames = 'username.json'
 # 打开文件，写入文件
with open(filenames,'w') as file_object:

    # 将用户输入的数据存储到username.json，dump(转储)
    json.dump(username,file_object) 
    print('We will remember you when you come back, ' + username + '!')



# 使用load读取前面写入的文件

import json

filename_useload = 'username.json'

with open(filename_useload) as file_uname:
    # 使用load指定读取的文件，存储到变量中
    userone = json.load(file_uname) 
    print('Welcome back, ' + userone + "!")




print('\n10.4.2.1')
 # 使用try合并dump和load
filename_try = 'username.json'  # 指定文件

 # 异常
try:

    # 打开文件，将一系列操作存储到
    with open(filename_try) as file_obj: # with后面的语句被求值后调用enter()方法，将enter方法返回值赋值到as后面的变量中
        username_try = json.load(file_obj) # 文件存在就将其中数据读取到内存中

 # 如果文件不存在，执行以下代码
except FileNotFoundError:
 # 获取用户输入，存储到变量中
    username_try = input('What is your name?')

    with open(filename_try,'w') as file_obj:
        # 使用json.dump()将用户输入转储到文件和变量中
        json.dump(username_try,filename_try)
        print('我认为你会回来的，' + username_try + '!')

else:
    print('欢迎回来，' + username_try + '!')















print('\n10.4.3')

# 10.4.3  重构 
 # 代码可以正常运行，但是可做进一步改进——将代码划分为一系列完成具体工作的函数。
 # 这样的过程被称为重构


 # 将大部分逻辑放到多个函数里

 # 相关查看refactor.py