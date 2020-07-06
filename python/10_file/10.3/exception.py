# 10.3 异常
# 异常：特殊对象
# 如果编写了处理该异常的代码，程序将继续运行
# 异常使用try-except代码块处理





print("10.3.1-2")
# 10.3.1-2  处理ZeroDivisionError异常

# 不能将一个数字除以0

# 用try - except代码块来自定义错误提示

# 如果try代码块中代码没错，Python将跳过except代码块，如果错了，Python将执行except
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("不能除以0")








# 10.3.3 使用异常避免崩溃

# print("Give me two numbers, and I`ll divide them.")
# print("Enter 'q' to quit.")

# try:
#     while True:
#         first_number = input("\nfirst number is: ")
#         if first_number == 'q':
#             break
#         second_number = input('Second number:')
#         if second_number == 'q':
#             break
#         answer = int(first_number) / int(second_number)
#         print(answer)
# except ZeroDivisionError:
#     print("不能除以0")  # 不能让用户看见traceback，也会暴漏系统安全性








print('\n10.3.4')
10.3.4 else代码块

print("Give me two numbers, and I`ll divide them.")
print("Enter 'q' to quit.")


while True:
    first_number = input("\nfirst number is: ")
    if first_number == 'q':
        break
    second_number = input('Second number:')
    if second_number == 'q':
        break

    # python尝试执行try代码块中的代码，只有可能引发异常的代码才放在try语句中
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError: # 出现异常时输出数据
        print("相除不能为0！")

    # 仅在try代码块成功执行时才需要运行的代码，这些代码放在else代码块中
    else: 
#         print(answer)   
        














print('\n10.3.5')
# 10.3.5 -----处理FileNotFoundError异常

 # 使用文件时，一种常见的问题是找不到文件


filename = 'blice.txt'

 # try代码块引发FileNotFoundError异常，python找出与该错误匹配的except代码块
try:
    with open(filename) as f_obj:
        contents = f_obj.read()

 # 异常运行下面代码块
except FileNotFoundError: 
    msg = "没有找到这个文件！"     
    print(msg)


















print('\n10.3.6')
# 10.3.6 -------分析文本

 # 获得一个文件有多少个单词

filename_alice = 'alice.txt'

try:
    with open(filename_alice) as file_alice:
        ctet = file_alice.read()
except FileNotFoundError:
    print("没有找到该文件")

else:
    # 计算文件大概有多少单词
    words = ctet.split()      # 。split()将包含字符串中所有单词的列表存储到变量中
    num_words = len(words)
    print("文件大概有 " + str(num_words) + "个单词。")


        













print('\n10.3.7')
# 10.3.7 ---------代码可让多个文件使用
 
 # 这些代码与上面一致，只是我们将其移动到函数中，可复用
def count_words(filename_words):
    try:
        with open(file_word) as file_w:
            count = file_w.read()
    except FileNotFoundError:
        print("该文件不存在")
    
    else:
        word = count.split()
        num_word = len(word)
        print("该文件有" + str(num_word) + "个单词！")

# file_words = 'alice.txt'
# count_words(file_words)

filenames = ['ailce.txt','little_woman.txt','notfound.txt']

for file_word in filenames:
    count_words(file_word)  # 只要保证函数传递的字段能和open里的字段一致就可以使用







    




print('\n10.3.8')
# 10.3.8 -------失败时不提示

# try:
#     --snip--
# except FileNotFoundError:
#     pass   不提示








print('\n10.3.9')
# 10.3.9 ------------决定报告哪些错误
# 有些错误需要报告，有些错误则不需要报告

