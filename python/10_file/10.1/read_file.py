# 10.1 从文件读取数据

#  读取文件，可以一次性读取文件全部内容，也可以每次一行逐步读取




import os
print(os.getcwd()) # 打印当前工作路径,文件存放路径与文件工作路径不一致

# os.chdir('包含相应文件的目录')   # 修改文件的工作目录





# 10.1.1  读取整个文件

with open('pi_digits.txt') as file_object: # |函数open()接受一个参数：要打开的文件的名称
                                           # |Python在当前工作路径查找该文件，也可以用绝对路径来指定
                                           # |函数open()返回一个表示文件的对象，open（file.txt）返回一个代表文件file.txt的对象
                                           # |Python将这个对象存储在我们将在后面使用的变量中 
                                            
                                           # |关键字with在不再需要访问文件后将其关闭


    contents = file_object.read() # 有了file.txt的文件对象后，使用方法read()读取这个文件全部内容，将其作为一个字符串存储到变量contents中
    print(contents.rstrip()) # 打印变量的值可将这个文本文件全部内容显示出来
  
  # 输出的文件末尾多了一个空行，因为read()到达文件末尾时返回一个空字符串，这个空字符串显示出来时一个空行
  # 空行可在print()语句中使用rstrip（）










