guest = ['A', 'B', 'C', 'D', 'E', 'F']
#    提示:同时使用字符串和 int 变量的概念中使用 + 时，Python无法正确理解意图 
#    如果希望将句子中的数字和字符串连接起来，就好像它们是单词一样，那么必须将数字从 int 格式转换为 string 格式，使用str()函数
print("I invited " + str(len(guest)) + " guests to the dinner.")
