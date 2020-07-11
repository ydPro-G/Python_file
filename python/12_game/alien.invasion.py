import sys # 导入模块

import pygame

def run_game():
    # 初始化游戏并创建一个屏幕对象,保持一个游戏窗口
    pygame.init() # 初始化背景设置
    screen = pygame.display.set_mode((1200,800))  # 调用pygame.display.set_mode创建一个名为scereen的显示窗口，所有图形元素都将在其中绘制
                                                  # 实参(1200，800)是一个元组，指定游戏窗口的尺寸
                                                  # 将这些尺寸值传递给pygame.display.set_mode()，我们创建了一个宽1200，高800的游戏窗口
                                                  # 对象screen是一个surface，在pygame中，surface是屏幕的一部分，用来显示游戏元素
                                                  # 每个元素都是一个surface，display.set_mode()返回的surface表示整个游戏窗口，每一次循环都将自动重绘整个surface,让它保持一直循环的状态
    pygame.display.set_caption('Alien Invasion')  # 游戏显示的标题
    bg_color = (230,230,230)

    # 开始游戏的主循环
    while True:
        
        # 监视键盘和鼠标事件，这是一个事件循环
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)    
        
        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()