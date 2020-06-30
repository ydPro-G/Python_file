import os
os.chdir('D:\\python_workbin')
filename = 'python.txt'

# 读取文件
with open(filename,encoding = 'utf-8') as file_object: # gbk修改为utf-8
    # 打印时读取整个文件
    contents = file_object.read()
    print(contents)




print("\n遍历文件对象")

with open(filename,encoding = 'utf-8') as for_file:
    # 打印时遍历文件对象
    for file_a in for_file:
        print(file_a.strip())
    



print("\n代码外打印")
with open(filename,encoding = 'utf-8') as intter:

    
    # 打印时将各行存储在一个列表中，再在with代码外打印它们
    lines = intter.readlines() # 读取每一行存储到列表中

for line in lines:
    print(line.strip()) 
















