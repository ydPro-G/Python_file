import pygame

class Ship():
    
    def __init__(self,screen):   # _init_()接受两个参数，引用self和screen,screen指定了要将飞船绘制到什么地方
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp') # pygame.image.load返回一个表示飞船的surface,我们将这个surface存储到self.image中
        self.rect = self.image.get_rect() # 使用get_rect()获取相应surface的属性rect（矩形），pygame能像处理矩形对象一样处理游戏元素
                                          # 处理rect()对象时,可使用矩形四角和中心的xy坐标，通过设置这些值来指定矩形的位置
        self.screen_rect = screen.get_rect()  # 表示屏幕的矩形存储在self.screen_rect中


        # 将每艘新飞船放在屏幕  底部bottom  中央centerx

        # 将self.rect.centerx（飞船中心的x坐标） 设置为表示屏幕的矩形的属性centerx  飞船在屏幕中间
        self.rect.centerx = self.screen_rect.centerx # 居中属性：center,centerx，centery
        
        # 将self.rect.bottom（飞船下边缘的y坐标） 设置为表示屏幕矩形的属性bottom   飞船下边缘在屏幕下方
        self.rect.bottom = self.screen_rect.bottom # 游戏元素与屏幕边缘对齐，使用属性top,bottom,left,right
                                                   # 要调整游戏元素的水平或垂直位置，可使用属性x，y,它们分别对应矩形左上角的x和y坐标
                                                   # 在pygame中原点(0,0)位于屏幕左上角，向右下方移动时，坐标值将增大;左上角（0,0）——右上角（1200,800）
    
        # 移动标志
        self.moving_right = False # 属性初始值为false
        self.moving_left = False

    def update(self): # 方法update，在前述标志为True时移动飞船
        """根据移动标志调整飞船的位置"""
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1








    # 定义方法biltme(),根据self.rect指定的位置将图像绘制到屏幕上
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)