everything = ['dongjing', 'beijing', 'shanghai',
              'qingdao', 'shenzhen', 'changjiang', 'huanghe']
print(everything)

print(everything[0])

print("\nThis is last " + everything[-1].title() + ".")

one = "\nThis is three word " + everything[2].title() + "."
print(one)

everything[0] = "xizang"
print("\nThe frist element is changed to " + everything[0].title() + ".")

#    这种创建列表的方式极其常见，因为经常要等程序运行后，你才知道用户要在程序中存储哪些数据。为控制用户，可首先创建一个空列表，用于存储用户将要输入的值，然后将用户提供的每个新值附加到列表中。
#    添加到最后
everything.append('henan')
print("\nUse the method .append() to add element " +
      everything[-1].title() + " the end.")

#   插入添加inster
everything.insert(1, 'hainan')
print("\nUse the methed .insert() insert element " +
      everything[1].title() + " the any location.")

print("\n")
print(everything)

#   删除
del everything[0]
print("Delete element 0 from the list using the del [] statement.")

#   pop弹出
print("\n")
poped_two = everything.pop(1)  # 如果没有指定，从最后面弹出到最前面
print("Use the methed .pop(1) to popup element " + poped_two + ".")
print(everything)

print("\n")
print(everything)
#    我们将值'qingdao'存储在变量remove_qingdao中（）。接下来，我们使用这个变量来告诉Python将哪个值从列表中删除。最后，值'qingdao'已经从列表中删除，但它还存储在变量remove_qingdao中.
remove_qingdao = 'qingdao'   # r = 'aa'  ever.remove(r)
everything.remove(remove_qingdao)
print("Use the methed .remove() remove element " + remove_qingdao + ".")
print(everything)

print("\n")
print(everything)
#    .sort()方法，对列表元素按照字母顺序永久性排序 a.sort()
everything.sort()
print(everything)

print("\n")
#    .sort(reverse=True)方法，将列表元素按照字母顺序相反的顺序永久性排序   a.sort(reverse=True)
everything.sort(reverse=True)
print(everything)

print("\n")
#   sorted()函数，对列表元素按照字母顺序临时性排序  print(sorted(aa))
print(sorted(everything))
print(sorted(everything))

print("\n")
#    sorted( ,reverse=True)函数，将列表元素按照字母顺序相反的顺序临时性排序   print(sorted(aa,reverse=True))
print(sorted(everything,reverse=True))

print("\n")
everything_new = ['hainan', 'shanghai', 'qingdao', 'shenzhen', 'changjiang', 'huanghe', 'henan']
#    .reverse()方法，永久性反转列表元素的排列顺序 
everything.reverse()
print(everything)

print("\n")
#    .reverse()方法，恢复到原来的排列顺序
everything.reverse()
print(everything)

print("\n")
#    len()函数，确定列表的长度
print(len(everything))
lne_0 = [1,2,3]
lne_0.reverse()
print(lne_0)
print(len(lne_0))





# 引用 
spam = [1,2,3]
chese = spam
chese[1] = 'hello'
print(spam)
# spam = [1, 'hello', 3]

# 将列表赋给一个变量时，实际上是将列表的索引赋值给了该变量，他们指向的还是同一内存地址写入的数据


# 变量保存可变数据类型的值时，例如字典和列表就使用索引
# 变量保存不可变的数据类型的值的时候，例如字符串，整数或元组，变量就保存值本身







# PS1： isX查看是否包含各种数据
# isalpha() 返回 True，如果字符串只包含字母，并且非空；
# isalnum() 返回 True，如果字符串只包含字母和数字，并且非空；
# isdecimal() 返回 True，如果字符串只包含数字字符，并且非空；
# isspace() 返回 True，如果字符串只包含空格、制表符和换行，并且非空；
# istitle() 返回 True，如果字符串仅包含以大写字母开头、后面都是小写字母的单词。

 # 验证用户输入知道答对
 
while True:
      print('Enter your age:')
      age = input()
      if age.isdecimal():
            break
      print('Please enter a number for your age.')

while True:
      print('Select a new password:')
      password = input()
      if password.isalnum():
            break
      print('Passwords!')






# PS2： startswith()和endswith() 开始关联，结束关联

'Hello world!'.startswith('Hello') # 开始关联
'Hello world!'.startswith('world') # 结束关联







# PS3: join()和split() 
 # join 在一个字符串上调用，参数是一个字符串列表，返回一个字符串，返回字符串由传入的列表每个字符串连接而成
 'ABC'.join(['my','name','is','simple'])
  #  'MyABCnameABCisABCSimon'
 
 # split()针对一个字符串调用，返回一个字符串列表
'my name is'.split()
['my','name','is']






# PS4 ： ljust(),rjust,center() 三种方法对齐文本
# ljust() ： 左对齐
# rjust() ： 右对齐
# center() : 中间对齐

print('hello'.rjust(10))#     hello
'hello'.ljust(10,'-') # 'hello----------' 
'Hello'.center(20, '=')
# '=======Hello========'







# PS5 ： 用 pyperclip 模块拷贝粘贴字符串
import pyperclip
pyperclip.copy('hello world') # 向计算机的剪贴板发送文本

pyperclip.paste() # 从剪贴板接收文本






# PS6 ： 正则表达式

# ? 匹配零次或一次前面的分组。
# * 匹配零次或多次前面的分组。
# + 匹配一次或多次前面的分组。
# {n} 匹配 n 次前面的分组。
# {n,} 匹配 n 次或更多前面的分组。
# {,m} 匹配零次到 m 次前面的分组。
# {n,m} 匹配至少 n 次、至多 m 次前面的分组。
# {n,m}? 对前面的分组进行非贪心匹配。
# ^spam 意味着字符串必须以 spam 开始。
# spam$ 意味着字符串必须以 spam 结束。
# . 匹配所有字符，换行符除外。
# \d 、\w 和 \s 分别匹配数字、单词和空格。
# \D 、\W 和 \S 分别匹配出数字、单词和空格外的所有字符。
# [abc] 匹配方括号内的任意字符（诸如 a、b 或 c）。
# [^abc] 匹配不在方括号内的任意字符。



# 1
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1) # 获取415
mo.group(2) # 获取555-4242
mo.group() # 获取415-555-4242
mo.groups() # 获取所有分组，('415', '555-4242')

# 2  | 管道

# 3 ？ 可选匹配
 batRegex = re.compile(r'Bat(wo)?man')
 mo1 = batRegex.search('The Adventures of Batman')
 mo1.group()
'Batman'

 mo2 = batRegex.search('The Adventures of Batwoman')
 mo2.group()
'Batwoman'


# 4 * 匹配零次或多次
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
'Batwoman'

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
'Batwowowowoman'