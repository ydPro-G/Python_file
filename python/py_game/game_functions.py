#   包含一系列函数，函数chech_events检测相关事件，如按键和松开
#   使用辅助函数check_keydown_events()和check_keyup_events来处理这些事件
#   函数update_screen()，每次执行主循环都重绘屏幕
import sys
import pygame
from bullet import Bullet # 导入子弹类


 

# 重构函数，一个响应KEYDOWN事件，一个响应KEYUP事件
def check_keydown_events(event,ship,ai_settings,screen,bullets): # 编组传递给了check_keydown_events
    """按下键盘触发KEYDOWN事件,true,开始移动"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # 子弹设置
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings,screen,ship) # 玩家按空格时创建一个新的子弹实例
        bullets.add(new_bullet) # 使用add()将实例添加到编组中

def check_keyup_events(event,ship):
    """松开键盘触发KEYUP事件,flase，结束移动"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


 # 包含形参ship，用来接收实参
def check_events(ai_settings,screen,ship,bullets): # 添加形参bullets
    """响应按键与鼠标事件"""
    for event in pygame.event.get(): # 通过pygame.event.get()方法获取事件，促使for循环运行
        if event.type == pygame.QUIT:
            sys.exit()

        # 判断:如果是KEYDOWN就调用keydown函数
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,ai_settings,screen,bullets)
        # 判断:如果是KEYUP调用keyup函数
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)



def update_screen(ai_settings,screen,ship,bullets): # 添加形参bullets
    """更新屏幕上的图像，并切换到新屏幕"""

    #每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites(): # 方法bullets.sprites返回一个列表，其中包含了bullets中的所有元素
        bullet.draw_bullet()
    ship.blitme()# 将飞船绘制到屏幕上

    # # 每次执行while循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见，移动游戏元素时，flip将不断更新屏幕，在原来位置隐藏元素
    pygame.display.flip()
        