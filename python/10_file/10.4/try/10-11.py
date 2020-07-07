import json

user_number = int(input("请输入喜欢的数字："))

filename = 'like_number.json'


# 将这个数字转储到文件里；dump

with open(filename,'w') as f_obj:
    json.dump(user_number,f_obj)


# 将文件里的数字读取到变量中；load
with open(filename) as f_obj:
    message = json.load(f_obj)
    print("I like your favorite number!It`s " + str(message) + ".")