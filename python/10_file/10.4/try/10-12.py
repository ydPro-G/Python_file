import json



filename = 'like_number.json'

# 如果json文件中存储了数字就显示出来，如果文件没有存储数字就提示用户输入然后转储到json文件中
try:
    with open(filename) as f_obj:
        message = json.load(f_obj)
        print("I know your favorite number!It`s: " + str(message))
# 如果没有就提示添加一个数字，然后转储到文件中
except FileNotFoundError:
    user_number = input("请输入你喜欢的数字:")
    with open(filename,'w') as f_object:
        json.dump(user_number,f_object)
        print("新添加数字：" + user_number)
          