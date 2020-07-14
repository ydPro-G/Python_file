# 重构既有代码，简化既有代码的结构
# 存储让游戏运行的函数，通过创建本模块，可避免alien_invasion.py太长


# 将管理事件的代码移到一个名为check_events()的函数中，简化run_game()并隔离事件管理循环
# 通过隔离事件循环，可将事件管理与游戏的其他方面分离


import sys

import pygame
from ship import Ship

def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



# 将更新屏幕的代码放入到一个update_screen()的函数中

def update_screen(ai_settings,screen,ship): #将主模块中的更新屏幕的代码替换为对函数update_screen()的调用
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 调用ship.blitme()将飞船绘制到屏幕上
    ship.blitme()

    # 让最近绘制的屏幕可见
    # 让最近绘制屏幕可见，每次执行while循环时都绘制一个空屏幕，并擦去就名目，使得只有新屏幕可见
        # 在移动游戏元素时，pygame.display.flip()将不断跟新屏幕，显示元素新位置，并在原来的位置隐藏元素，从而营造平滑移动的效果
    pygame.display.flip()