def make_ablum(singer_name,ablum_name):   # 字典默认值
    message = {'singer name: ': singer_name,'album name: ': ablum_name}  # 字典也一样用

    return message

while True:
    print("enter 'q' quit!")
    sing_name = input("singer name is ")
    if sing_name == 'q':
        break
    ab_name = input("ablum name is ")
    if ab_name == 'q':
        break
    b = make_ablum(sing_name,ab_name)  # 如果没有缩进，他就和while无关，所以会获取q
    print(b)




