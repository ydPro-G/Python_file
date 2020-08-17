#   Ship类，类包含方法_init_()，管理飞船位置的方法update(),以及在屏幕上绘制飞船的方法blitme()


import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始设置"""
        self.screen = screen
        self.ai_settings = ai_settings # 获取形参的值存储到属性中,在update中使用它

        # 加载飞船图像并获取其外接矩形
        self.image =pygame.image.load('images/ship.bmp') # 获取一个表示飞船的surface,将这个surface存储到self.image中
        self.rect = self.image.get_rect() # 使用get_rect()获取相应surface（飞船图形）的属性rect——可供计算机理解的矩形对象
        self.screen_rect = screen.get_rect() # 获取screen(窗口)的rect——共计算机理解的矩形对象

        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx # 飞船的中心点在窗口的中心点，飞船的底部在窗口的底部
        self.rect.bottom = self.screen_rect.bottom  # 游戏元素居中：centerx——与屏幕边缘对齐：top，bottom，left，right
                                                    # 调整游戏元素水平或垂直位置：使用属性x或y——原点(0,0)位于屏幕左上角，右下角坐标位于最大值
        
        # 在飞船属性center中存储小数值，确保移动速度可以为小数
        self.center = float(self.rect.centerx) # 使用float将self.rect.centerx转换为小数，将结果储存在属性self.center中









        # 飞船移动方向及移动位置
        # 移动标志,初始值为False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志来调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right: # 1200  # 飞船移动的位置和飞船外接矩形的右边缘x坐标小于1200说明飞船未触及屏幕右边缘
            self.center += self.ai_settings.ship_speed_factor # 飞船中心坐标加setting中的飞船速度属性
        if self.moving_left and self.rect.left > 0:  # 左边缘的x坐标大于0，说明飞船未触及屏幕左边缘
            self.center -= self.ai_settings.ship_speed_factor # 向左移动
        
        # 根据self.center更新rect对象
        self.rect.centerx = self.center
        

  

        
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect) # 根据self.rect指定的位置将图像绘制到屏幕上