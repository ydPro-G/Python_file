import pygame

class Ship():
    def __init__(self,screen):
        """初始化飞船并设置其初始设置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image =pygame.image.load('images/ship.bmp') # 获取一个表示飞船的surface,将这个surface存储到self.image中
        self.rect = self.image.get_rect() # 使用get_rect()获取相应surface的属性rect——可供计算机理解的矩形对象
        self.screen_rect = screen.get_rect() # 获取screen(窗口)的rect——共计算机理解的矩形对象

        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx # 飞船的中心点在窗口的中心点，飞船的底部在窗口的底部
        self.rect.bottom = self.screen_rect.bottom  # 游戏元素居中：centerx——与屏幕边缘对齐：top，bottom，left，right
                                                    # 调整游戏元素水平或垂直位置：使用属性x或y——原点(0,0)位于屏幕左上角，右下角坐标位于最大值



    