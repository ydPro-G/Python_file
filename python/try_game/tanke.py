import pygame

class Tanke():
    def __init__(self,screen):

        self.screen = screen  # 属性=形参
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    
    def blitme(self):
        """在指定位置绘制坦克"""
        self.screen.blit(self.image,self.rect)

