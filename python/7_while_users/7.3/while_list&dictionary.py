# 7.3 使用while循环来处理列表和字典

# 7.3.1 在列表之间移动元素  在验证用户的同时将其从未验证用户列表中提取出来，加入到另一个已验证用户列表
print("7.3.1")

# 首先， 创建一个待验证用户列表
# 其次， 创建一个用于存储已验证用户的空列表
unconfirmed_users = ['alice','brian','candace'] 
confirmed = []

# 验证每个用户， 直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:  #while循环不断运行，直到列表为空
    current_user = unconfirmed_users.pop() # 函数pop()以每次一个的方式从列表末尾删除未验证的用户
                                           # 由于candcace位于列表末尾，因此将首先被删除，储存到变量中
                                            
    print("Verifying user: " + current_user.title())
    confirmed.append(current_user) # 添加到列表中

# 显示所有已验证用户
print("\nThe following users have been confirmed:")
for confirmed_0 in confirmed:
    print(confirmed_0.title())


