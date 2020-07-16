# import sys
# import pygame

# def run_game():
#     # 初始化设置
#     pygame.init()
#     # 窗口大小
#     screen = pygame.display.set_mode((1200,800)) # display.set_mode方法设置窗口大小，存储在对象screen中，对象screen时一个surface，surface时屏幕的一部分，用于显示游戏元素，每个游戏元素都是一个surface
#     # 窗口标题
#     pygame.display.set_caption("Alien Invasion") # display.set_caption()方法设置标题文字
#     # 窗口背景色
#     bg_color = (230,230,230)
    
#     # 开始游戏主循环
#     while True:

#         # 监视键盘和鼠标事件
#         for event in pygame.event.get(): # 为了访问
#             if event.type == pygame.QUIT:
#                 sys.exit()


#         # 填充背景色,只接受一个实参，一种颜色
#         screen.fill(bg_color)


#         # 每次执行while循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见，移动游戏元素时，flip将不断更新屏幕，在原来位置隐藏元素
#         pygame.display.flip()

# run_game()





import sys
import pygame
from settings import Settings

def run_game():
    # 初始化设置
    pygame.init()
    ai_settings = Settings()
    # 窗口大小
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)) # display.set_mode方法设置窗口大小，存储在对象screen中，对象screen时一个surface，surface时屏幕的一部分，用于显示游戏元素，每个游戏元素都是一个surface
    # 窗口标题
    pygame.display.set_caption("Alien Invasion") # display.set_caption()方法设置标题文字
    
    
    
    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get(): # 为了访问
            if event.type == pygame.QUIT:
                sys.exit()


        # 填充背景色,只接受一个实参，一种颜色
        screen.fill(ai_settings.bg_color)


        # 每次执行while循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见，移动游戏元素时，flip将不断更新屏幕，在原来位置隐藏元素
        pygame.display.flip()

run_game()