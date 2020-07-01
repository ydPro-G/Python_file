import os
print(os.getcwd())






filename = 'guest.txt'

with open(filename,'w',encoding='utf-8') as file_object:
    name_input = input('请输入名字：') # 获取用户输入
    file_object.write(name_input)
    
    
        
    
        
    



    

