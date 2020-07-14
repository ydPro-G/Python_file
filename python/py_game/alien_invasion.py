import sys
import pygame
from settings import Settings

def run_game():
    # 初始化pygame，设置和屏幕对象
    pygame.init()
    ai_settings = Settings() # 创建一个Settings实例，并将其存储在变量ai_settings中

    # 调用方法创建一个名为screen的显示窗口，对象screen市一个surface，surface是屏幕的一部分，用于显示游戏元素
    # 每个元素都是一个surface，display.set_mode()返回的surface表示整个游戏窗口
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))

    # 设置屏幕显示标题
    pygame.display.set_caption("Alien Invasion")


    # 开始主游戏循环
    while True:

        # 监视鼠标和键盘事件,单击游戏窗口的关闭按钮，将检测到pygame.QUIT()事件，调用sys.exit()退出游戏
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 在每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        
        # 让最近绘制屏幕可见，每次执行while循环时都绘制一个空屏幕，并擦去就名目，使得只有新屏幕可见
        # 在移动游戏元素时，pygame.display.flip()将不断跟新屏幕，显示元素新位置，并在原来的位置隐藏元素，从而营造平滑移动的效果
        pygame.display.flip()


run_game()


