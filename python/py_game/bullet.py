import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):  # 继承了导入的类，将游戏中相关的元素编组，并同时操作编组中的所有元素
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self,ai_settings,screen,ship):# 传递ai_settings,screen和ship实例
        """在飞船所处的位置创建一个子弹对象"""
        super().__init__() # 调用super()来继承Sprite
        self.screen = screen

        # 在(0，0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
        ai_settings.bullet_height)        # 创建子弹的属性rect，子弹并非是基于图像，因此我们必须使用pygame.Rect()从空白创建一个矩形
                                          # 提供矩阵左上角x坐标和y坐标，还有矩形的宽度和高度
        self.rect.centerx = ship.rect.centerx  # 将子弹的centerx设置为飞船的rect.centerx
        self.rect.top = ship.rect.top # 子弹从飞船顶部发射，所以子弹的rect的top属性为飞船的rect的top属性

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)  # 将子弹的y坐标存储为小数值，以便能微调子弹速度

        self.color = ai_settings.bullet_color # 子弹颜色设置存储到self.color
        self.speed_factor = ai_settings.bullet_speed_factor # 子弹速度设置存储到self.speed_factor

    
    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor  # 发射出去后子弹向上移动，y坐标不断缩小，为更新子弹位置，从self.y中减去原来的位置
        # 更新表示子弹的rect的位置
        self.rect.y = self.y # 将self.rect.y设置为self.y的值

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect) # 使用存储的颜色填充表示子弹的rect占据的屏幕部分
