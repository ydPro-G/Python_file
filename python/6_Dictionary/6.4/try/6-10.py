like_num = {
    'A': [1,2,3],
    'B': [4,5,6],
    'C': [7,8,9],
}
for name,num in like_num.items():
    print("name is:" + name)
    for n in num:
        print("like number is:" + str(n))  # 考察的是对str的使用
