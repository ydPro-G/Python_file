# 10.2 写入文件
# 读取模式 1.读取模式('r')
# 读取模式 2.写入模式('w')
# 读取模式 3. 附加模式('a')
# 读取模式 4. 读取和写入模式('r+')
# 在with语句里操作循环写入，(while和for)
import os
print(os.getcwd())






# 10.2.1 写入空文件
filename = 'programming.txt'

with open(filename,'w') as file_object:  # 1. 指定文件 2. 指定模式 w（写入模式）
    file_object.write('I LOVE PROGRAMMING.\n')









# 10.2.2 写入多行
# 在字符串末尾加换行符[\n]
    file_object.write('one\n')
    file_object.write('two\n')







# 10.2.3 附加到文件 
# 为文件添加内容，而不是覆盖原有的内容，使用附加模式('a')
file_pro = 'programming.txt'

with open(file_pro,'a') as file_addtiion: # a 附加模式
    file_addtiion.write('three\n')
    file_addtiion.write('four\n')