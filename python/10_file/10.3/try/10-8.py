def file_notFound(filenames):
    try:
        with open(filename,encoding='utf-8') as file_object:
            contunt = file_object.read()
            for cont in contunt:
                print(cont.rstrip())
    except FileNotFoundError:
        print('FILENOTFOUND!')

filenames = ['cats.txt','dogs.txt','notfound.txt']

for filename in filenames:
    file_notFound(filename)