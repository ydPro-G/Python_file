def sanwich(*food):
    """
    顾客点的三明治进行概述
    """
    print(food)  # 元组不能和字符串一起使用

sanwich('青椒三明治') # 注意要调用函数才能运行函数体
sanwich('胡罗卜三明治','火腿三明治')


# 美化
def sandwich(*foods):
    """
    顾客要点多少三明治
    """
    print("顾客要点的三明治有：")
    for food_1 in foods:
        print("- " + food_1)

sandwich("ONE")
sandwich('two','three')