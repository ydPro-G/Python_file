favorite_places = {
    'Zhao': ['BJ','SH','SZ'],
    'Qian': ['GZ','SH','HZ'],
    'Sun': ['BJ','TJ','QD'],
}
for name,places in favorite_places.items():
    print("name is: " + name.title())
    for place in places:
        print("favorite places is:" + place)

        # 键是单一的，而值是列表，
        # 使用方法.items()返回键值对列表
        # 使用for循环将每一个键中的值（列表），储存在临时变量中输出，接着进行这个循环