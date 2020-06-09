def car(makeer,types,**everything):
    """
    接受制造商和型号,还接受任意数量的关键字实参
    """
    cars = {} # 先声明它是字典

    cars['制造商'] = makeer, #再添加键值对
    cars['类型'] = types,
    for keys,value in everything.items():
        cars[keys] = value
    
    return cars

a = car('a','1',color='red')
b = car('b','2',color='green')
print(a,b,sep='\n')