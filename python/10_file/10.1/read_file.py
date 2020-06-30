# 10.1 从文件读取数据

#  读取文件，可以一次性读取文件全部内容，也可以每次一行逐步读取




import os
print(os.getcwd()) # 打印当前工作路径,文件存放路径与文件工作路径不一致

os.chdir('D:\\python_workbin')   # 修改文件的工作目录


# with open(filename,encoding = 'utf-8') as file_object   修改gbk错误







# 10.1.1  读取整个文件

with open('pi_digits.txt') as file_object: # |函数open()接受一个参数：要打开的文件的名称
                                           # |Python在当前工作路径查找该文件，也可以用绝对路径来指定
                                           # |调用open()后，将一个表示文件及其内容的对象存储到变量file_object中
                                           # |Python将这个对象存储在我们将在后面使用的变量中 
                                            
                                           # |关键字with在不再需要访问文件后将其关闭


    contents = file_object.read() # 有了file.txt的文件对象后，使用方法read()读取这个文件全部内容，将其作为一个字符串存储到变量contents中
    print(contents.rstrip()) # 打印变量的值可将这个文本文件全部内容显示出来
  
  # 输出的文件末尾多了一个空行，因为read()到达文件末尾时返回一个空字符串，这个空字符串显示出来时一个空行
  # 空行可在print()语句中使用rstrip（）









# 10.1.2 文件路径
# 可以使用相对路径也可以使用绝对路径








# 10.1.3 逐行读取
# 可能需要检查每一行，查找特定信息修改特定信息
# 可以使用for循环
print("\n10.1.3")

filename = 'pi_digits.txt'  # 将要读取的文件名存储到变量filename中，变量filename表示的并非实际文件，它只是一个让Python知道去哪里查找文件的字符串

with open(filename) as file_objects:  # 调用open()后，将一个表示文件及其内容的对象存储到变量file_object中
  for line in file_objects: # 对文件对象执行循环来遍历文件中的每一行
    print(line.rstrip()) 
    # 打印后出现空白行，因为在每行末尾都有一个看不见的换行符，print语句也会加上一个换行符，因此，每行末尾都有两个换行符，一个来自文件，另一个来自print语句
    # 要消除空白行可在print语句中添加rstrip()











# 10.1.4 创建一个包含文件各行内容的列表
 # 使用with时，open返回的文件对象只在with代码块内可用
 # 如果要在with代码块外访问文件内容，可在with代码块内将文件的各行存储在一个列表中。并在with代码块外使用该列表

with open(filename) as file_ob:

  lines = file_ob.readlines() # 方法readlines()从文件中读取每一行，将其存储在列表l中

for l in lines: # 列表被存储到变量lines中

  print(l.rstrip()) # 在with代码块外，我们仍可以使用变量




# strrip()去除所有空格
# rstrip()去除末尾空格




# 10.1.5 使用文件的内容
# 将文件读取到内存后，就可以以任何方式使用这些数据
print('\n10.1.5')

pi_string = '加' # 创建一个变量用来存储文件中的值
for lin in lines: 
  pi_string += lin.strip() # 使用一个循环将各行都加入pi_string，并删除末尾的换行符

print(pi_string) # 打印这个变量
print(len(pi_string)) # 打印他的长度











# 10.1.6 包含一百万位的大型文件
 # 对于可处理的数据量，Python没有任何限制

print("\n10.1.6")

filename_a = 'pimillion_digits.txt'

with open(filename_a) as file_a:
  lines_a = file_a.readlines()

pi_string_a = '' # 创建一个变量用来存储文件的值
for line_a in lines_a:
  pi_string_a += line_a.strip()

print(pi_string_a[:52] + "......")
print(len(pi_string_a))











# 10.1.7 圆周率值中包含你的生日吗？
birthday = input("Enter your birthday,in the form mmddyy: ") # 提醒用户输入
if birthday in pi_string_a: # 检查这个字符串是否包含在pi_string中
  print("Yes!")

else:
  print("No!")



