def make_shirt(size,typeface):
    """T恤的尺码和字样"""
    print("T-shirt size is " + size + ",typeface is " + typeface + ".")

make_shirt('9','Fate') # 位置实参
make_shirt(size='11',typeface='nice') # 关键字实参
