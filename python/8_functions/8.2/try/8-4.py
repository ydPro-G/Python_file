def make_shirt(size,typeface='dog'):
    """一件默认字样的大号T恤，意见默认字样的中号T恤，一件其他字样的T恤"""
    print("T-shirt size is " + size + ",typeface is " + typeface + ".")

make_shirt('large size')# 默认值
make_shirt('medium')# 默认值
make_shirt('small',typeface='cat')# 关键字实参