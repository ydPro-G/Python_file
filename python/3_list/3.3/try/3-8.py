travel = ['dongjing', 'shanghai', 'qianye', 'bali', 'nvyue']
#    按照原始顺序打印该列表
print(travel)
#    使用sorted()函数按字母顺序打印该列表
print(sorted(travel))
#    再次打印该列表，核实排列顺序未变
print(travel)
#    使用sorted(reverse=True)函数按与字母顺序相反的顺序打印该列表
print(sorted(travel, reverse=True))
#    再次打印该列表，核实排列顺序未变
print(travel)
#    使用reverse()方法倒着打印列表，永久性修改列表元素的排序
travel.reverse()
print(travel)
#    使用reverse()再次打印列表，核实其已回复到原来的排列顺序
travel.reverse()
print(travel)
#    使用sort()修改该列表，让其元素按字母顺序永久排序
travel.sort()
print(travel)
#    使用sort(reverse=True)
travel.sort(reverse=True)
print(travel)

