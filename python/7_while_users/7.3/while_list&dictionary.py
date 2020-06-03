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




















#7.3.2 删除包含特定值的所有列表元素
print("\n7.3.2")
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets: # cat在列表中，一直循环
    pets.remove('cat')  #删除cat，直到没有cat结束循环

print(pets)











#7.3.3 使用用户输入来填充字典
print("\n7.3.3")
responses = {} #创建一个空字典

# 设置一个标志，指出调查是否继续
polling_active =True  # 标志，只要为true就一直循环

while polling_active:
    name = input("\nWhat is your name? ") # 提示输入被调查者的名字和回答
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response  # 将答案存储在字典中，键值对列表，name键，response值

# 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no': # 检查条件
        polling_active = False   #询问是否还有人参与调查，yes继续while循环，no，标志为False，结束循环


# 调查结束，显示结果
    print("\n--- Poll Results ---")
    for name,response in responses.items(): # 输出从用户哪里获得的键，值
        print(name + " Would like to climb " + response + ".")



   
