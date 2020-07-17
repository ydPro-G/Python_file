import sys
import pygame


 # 包含形参ship，用来接收实参
def check_events(ship):
    """响应按键与鼠标事件"""
    for event in pygame.event.get(): # 通过pygame.event.get()方法获取事件，促使for循环运行
        if event.type == pygame.QUIT:
            sys.exit()

        # 按下键盘触发KEYDOWN事件,true,开始移动
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        # 松开键盘触发KEYUP事件,flase，结束移动
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
        





def update_screen(ai_settings,screen,ship):
    """更新屏幕上的图像，并切换到新屏幕"""

    #每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()# 将飞船绘制到屏幕上

    # # 每次执行while循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见，移动游戏元素时，flip将不断更新屏幕，在原来位置隐藏元素
    pygame.display.flip()
        