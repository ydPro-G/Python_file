#    4.1使用for循环遍历整个列表
magicians = ['alice','david','carolina']
#    让python从列表中取出一个字符，将其储存在临时变量中，接下来循环这个操作，直到列表中没有其他值
#    在这里，for循环后面没有其他代码，因此程序结束，如果有其它代码程序会再循环
for magician in magicians:
    print(magician)


#    4.1.2在for循环中执行更多的操作
print("\n4.1.2")
magicians = ['alice','david','carolina']
#    第一次迭代是'alice',第二次迭代是'david',第三次迭代是'carolina'
#    ！ ':' 号后面需要跟四个空格！ 
#    在for之后，每个缩进的代码行都是循环的一部分
for magician_1_2 in magicians:
    print(magician_1_2.title() + ", that was a great trick!")
    print("I can`t wait to see your next trick, " + magician_1_2.title() + ".\n")


#    4.1.3在for循环结束后执行一些操作
print("\n4.1.3")
magicians = ['alice','david','carolina']
for magician_1_3 in magicians:
    print(magician_1_3.title() + ", that was a great trick!")
    print("I can`t wait to see your next trick" + magician_1_3.title() + ".\n")
#   在for循环后面，没有缩进的代码都只执行一次，而不会重复执行
print("Thank you, everyone. That was a great magic show!")


#    4.2避免缩进错误
print("\n4.2")
#    4.2.1忘记缩进——>报错
#    4.2.2忘记缩进额外的代码行——>额外的代码行只执行一次
#    4.2.3不必要的缩进——>报错
#    4.2.4循环了不必要循环的缩进——>输出与预期不一致
#    4.2.5遗漏了冒号——>语法错误，报错
#     ^-^


