import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    
    def __init__(self,ai_settings,screen):
        """初始化外星人并设置其初始位置"""
        super(Alien,self).__init__()
        self.screen = screen   # 设置形参的属性
        self.ai_settings = ai_settings

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()  # 获取图片的矩形

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width # 外星人的左边距为外星人的宽度
        self.rect.y = self.rect.height # 上边距设置为外星人的高度

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)