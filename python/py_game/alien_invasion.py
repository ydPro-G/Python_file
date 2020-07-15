import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化pygame，设置和屏幕对象
    pygame.init()
    ai_settings = Settings() # 创建一个Settings实例，并将其存储在变量ai_settings中

    # 调用方法创建一个名为screen的显示窗口，对象screen是一个surface，surface是屏幕的一部分，用于显示游戏元素
    # 每个元素都是一个surface，display.set_mode()返回的surface表示整个游戏窗口
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))

    # 设置屏幕显示标题
    pygame.display.set_caption("Alien Invasion")


    # 创建一艘飞船
    ship = Ship(screen)  # 创建一个名为ship的Ship实例，必须在主循环前面创建该实例


    # 开始主游戏循环
    while True:
        

        # 监视鼠标和键盘事件,单击游戏窗口的关闭按钮，将检测到pygame.QUIT()事件，调用sys.exit()退出游戏
        gf.check_events(ship) # 更新调用的check_events代码，将ship作为实参传递给它
        ship.update()

        # 每次循环都重绘屏幕，让飞船显示在屏幕上，让最近绘制的屏幕可见
        gf.update_screen(ai_settings,screen,ship)


run_game()


