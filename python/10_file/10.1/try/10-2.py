import os
os.chdir('D:\\python_workbin')

filename = 'python.txt'


with open(filename,encoding='utf-8') as file_object:
    line = ''
    for file_a in file_object:
        line += file_a.rstrip()
        print(line.replace('python','c')) # print语句要包含在循环中


       