def build_profile(first,last,**user_info):   # 2个**号创建的是空字典，1个*号是空元组
    """
    创建一个字典，其中包含我们知道的有关用户的一切
    """
    profile = {}  # 函数体：创建一个空字典，存储用户简介
    profile['first_name'] = first # 将名加入这个profile字典
    profile['last_name'] = last   # 将姓加入这个profle字典
    for username,userinfo in user_info.items(): # 遍历字典user_info中的键值对
        profile[username] = userinfo # 将每个键-值对都加入到字典profile中

    return profile # 将字典profile返回给函数调用行
   


user_profile = build_profile('alis','cins',guan='22',sun='php') # 调用函数build_profile,向它传递名，姓和两个键-值对，将返回的profile字典存储在变量中
my_profile = build_profile('guan','xuetao',like='vtb',age='23',language='chinese')

print(user_profile) # 打印这个变量
print(my_profile)