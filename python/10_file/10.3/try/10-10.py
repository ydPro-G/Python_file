def frequency(filenames):
    try:
        with open(filename) as file_number:
            countent = file_number.read()
    except FileNotFoundError:
        print('该文件不存在')

    else:
        number = countent.lower().count('it')  # count 确定特定单词出现次数 lower 都转换为小写来比较
        print(number)


filename = 'alice.txt'
frequency(filename)