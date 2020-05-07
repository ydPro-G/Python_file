current_users = ['admin','user1','user2','user3','user4']
new_users = ['admin','user5','user6','user7','user8','ADMIN']

for new_user in new_users:
    if new_user.lower() in current_users:   #Python lower() 方法转换字符串中所有大写字符为小写。  这个临时变量不管大小写都比较他们是否在current_user中
        print("The user name " + new_user + " has been used.")
    else:
        print("The user name " + new_user.title() + " is not used.")
