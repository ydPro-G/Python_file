




#   添加射击功能，编写玩家按空格发射子弹的代码，子弹在屏幕中向上穿行，抵达屏幕边缘后消失
#   将子弹存储到编组中，这个编组是pygame.sprite.Group的一个实例
#   设置外星人实例
#   添加外星人移动限制
#   碰撞：游戏元素重叠在一起，使用sprite.groupcollide()检测子弹编组与外星人编组成员间的碰撞
#   生成新的外星人
#   外星人与飞船碰撞结束游戏
#   外星人到达屏幕底端结束游戏



import sys
import pygame
from pygame.sprite import Group # 编组类
from settings import Settings  # 所有设置的类
from ship import Ship # 飞船图像设置
from alien import Alien # 外星人的设置类
import game_functions as gf # 函数设置
from game_stats import GameStats





def run_game():

    # 初始化设置
    pygame.init()
    ai_settings = Settings()

    # 窗口大小
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) # display.set_mode方法设置窗口大小，存储在对象screen中，对象screen时一个surface，surface时屏幕的一部分，用于显示游戏元素，每个游戏元素都是一个surface
    
    # 窗口标题
    pygame.display.set_caption("Alien Invasion") # display.set_caption()方法设置标题文字
    
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)



    # 在循环外创建一艘飞船，一个子弹编组和一个外星人编组
    ship = Ship(ai_settings,screen)  # 为飞船速度传入实参ai_settings

    # 创建一个用于存储子弹的编组
    bullets = Group() # 导入pygame.sprite中的Group类，创建一个Groyp实例，将其命名为bullets
    aliens = Group() # 外星人的空编组
    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens) # 储存飞船对象的形参

    # 创建一个外星人实例
    alien = Alien(ai_settings,screen)

     



    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)

        bullets.update() # 将bullets传递给check_events和update_screen()
                         # 在check_events中，需要在玩家按空格处理bullets
                         # 对编组调用update时，编组自动对其中每个精灵调用update()，将为编组bullets中的每颗子弹调用bullet.update()

        if stats.game_active:
        # 飞船位置在检测到键盘事件后（更新屏幕前）更新
            ship.update()

        

        # 删除已消失的子弹
            gf.update_bullets(bullets,aliens,screen,ship,bullets)

        # 更新每个外星人的位置,使用这些实参跟踪玩家还有多少艘飞船，创建一群新外星人
            gf.update_aliens(ai_settings,aliens,ship,stats,screen,bullets)


        # 更新屏幕的图像，传递了一个外星人实例
            gf.update_screen(ai_settings,screen,ship,aliens,bullets)# 在update_screen中，需要更新绘制到屏幕上的bullets
                         

run_game()