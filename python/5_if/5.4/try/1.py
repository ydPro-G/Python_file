current_users=['John','B','c','d','e','h'] print(current_users) current_user=[]
#定义一个变量
 for x in current_users: current_user.append(x.lower())#将列表转化为小写 
 
 print(current_user)#测试是否转化了小写 
 print(current_users)#测试原列表是否没被更改 
 new_users=['JOHN','b','f','g','p'] for new_user in new_users :
  if new_user.lower() in current_user:#与转化了小写的current_user比较，少个s
   print(new_user + "," + "You should print other name.") 
   else : print(new_user + "," + "This name can use.")