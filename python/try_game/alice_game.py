import sys
import pygame
from tanke import Tanke

def run_game():

    # 1.初始化pygame
    pygame.init()

    # 2.设置窗口属性
    screen_width = 1200
    screen_height = 800
    bg_color = (255,255,255)

    screen = pygame.display.set_mode((screen_width,screen_height))

    # 设置窗口标题
    pygame.display.set_caption("AliceGame")
    
    tanke = Tanke(screen)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        tanke.blitme()

        # 蓝色
        screen.fill(bg_color)  # screen.fill 填充窗口，可以用背景色


        # 让最近绘制的屏幕可见
        pygame.display.flip()
                



run_game()