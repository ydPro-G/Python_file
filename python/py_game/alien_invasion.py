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





# import sys
# import pygame
# from settings import Settings  # 所有设置的类
# from ship import Ship # 飞船图像设置


# def run_game():
#     # 初始化设置
#     pygame.init()
#     ai_settings = Settings()
#     # 窗口大小
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width,ai_settings.screen_height)) # display.set_mode方法设置窗口大小，存储在对象screen中，对象screen时一个surface，surface时屏幕的一部分，用于显示游戏元素，每个游戏元素都是一个surface
#     # 窗口标题
#     pygame.display.set_caption("Alien Invasion") # display.set_caption()方法设置标题文字
    
#     # 在循环外创建一艘飞船
#     ship = Ship(screen)  # 将窗口属性传递给类
    
    
#     # 开始游戏主循环
#     while True:

#         # 监视键盘和鼠标事件
#         for event in pygame.event.get(): 
#             if event.type == pygame.QUIT:
#                 sys.exit()


#         # 每次循环时都重绘屏幕
#         screen.fill(ai_settings.bg_color)
#         ship.blitme() # 将飞船绘制到屏幕上


#         # 每次执行while循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见，移动游戏元素时，flip将不断更新屏幕，在原来位置隐藏元素
#         pygame.display.flip()

# run_game()




                            # 重构：模块game_functions


# import sys
# import pygame
# from settings import Settings  # 所有设置的类
# from ship import Ship # 飞船图像设置
# import game_functions as gf # 函数设置



# def run_game():
#     # 初始化设置
#     pygame.init()
#     ai_settings = Settings()
#     # 窗口大小
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width,ai_settings.screen_height)) # display.set_mode方法设置窗口大小，存储在对象screen中，对象screen时一个surface，surface时屏幕的一部分，用于显示游戏元素，每个游戏元素都是一个surface
#     # 窗口标题
#     pygame.display.set_caption("Alien Invasion") # display.set_caption()方法设置标题文字
    
#     # 在循环外创建一艘飞船
#     ship = Ship(screen)  # 将窗口属性传递给类
    
    
#     # 开始游戏主循环
#     while True:

#         # 监视键盘和鼠标事件
#         gf.check_events()
       

#         # 每次循环时都重绘屏幕
#         screen.fill(ai_settings.bg_color)
#         ship.blitme() # 将飞船绘制到屏幕上


#         # 每次执行while循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见，移动游戏元素时，flip将不断更新屏幕，在原来位置隐藏元素
#         pygame.display.flip()

# run_game()










#           # 将重绘屏幕的代码重构

# import sys
# import pygame
# from settings import Settings  # 所有设置的类
# from ship import Ship # 飞船图像设置
# import game_functions as gf # 函数设置



# def run_game():

#     # 初始化设置
#     pygame.init()
#     ai_settings = Settings()

#     # 窗口大小
#     screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) # display.set_mode方法设置窗口大小，存储在对象screen中，对象screen时一个surface，surface时屏幕的一部分，用于显示游戏元素，每个游戏元素都是一个surface
    
#     # 窗口标题
#     pygame.display.set_caption("Alien Invasion") # display.set_caption()方法设置标题文字
    
#     # 在循环外创建一艘飞船
#     ship = Ship(screen)  # 将窗口属性传递给类
    
    



#     # 开始游戏主循环
#     while True:

#         # 监视键盘和鼠标事件
#         gf.check_events(ship)
#         # 飞船位置在检测到键盘事件后（更新屏幕前）更新
#         ship.update()
#         # 更新屏幕的图像
#         gf.update_screen(ai_settings,screen,ship)

# run_game()









#   总结：创建一系列整个游戏都要用到的对象
#         存储到ai_sttings中的设置
#         存储在screen中的主显示surface以及一个飞船实例
#         包含游戏的主循环，这是一个调用check_events(),ship.update()和update.screen()的while循环

# import sys
# import pygame
# from settings import Settings  # 所有设置的类
# from ship import Ship # 飞船图像设置
# import game_functions as gf # 函数设置



# def run_game():

#     # 初始化设置
#     pygame.init()
#     ai_settings = Settings()

#     # 窗口大小
#     screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) # display.set_mode方法设置窗口大小，存储在对象screen中，对象screen时一个surface，surface时屏幕的一部分，用于显示游戏元素，每个游戏元素都是一个surface
    
#     # 窗口标题
#     pygame.display.set_caption("Alien Invasion") # display.set_caption()方法设置标题文字
    
#     # 在循环外创建一艘飞船
#     ship = Ship(ai_settings,screen)  # 为飞船速度传入实参ai_settings
    
    



#     # 开始游戏主循环
#     while True:

#         # 监视键盘和鼠标事件
#         gf.check_events(ship)
#         # 飞船位置在检测到键盘事件后（更新屏幕前）更新
#         ship.update()
#         # 更新屏幕的图像
#         gf.update_screen(ai_settings,screen,ship)

# run_game()














#   添加射击功能，编写玩家按空格发射子弹的代码，子弹在屏幕中向上穿行，抵达屏幕边缘后消失
#   将子弹存储到编组中，这个编组是pygame.sprite.Group的一个实例




import sys
import pygame
from pygame.sprite import Group # 编组类
from settings import Settings  # 所有设置的类
from ship import Ship # 飞船图像设置
import game_functions as gf # 函数设置




def run_game():

    # 初始化设置
    pygame.init()
    ai_settings = Settings()

    # 窗口大小
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) # display.set_mode方法设置窗口大小，存储在对象screen中，对象screen时一个surface，surface时屏幕的一部分，用于显示游戏元素，每个游戏元素都是一个surface
    
    # 窗口标题
    pygame.display.set_caption("Alien Invasion") # display.set_caption()方法设置标题文字
    
    # 在循环外创建一艘飞船
    ship = Ship(ai_settings,screen)  # 为飞船速度传入实参ai_settings

    # 创建一个用于存储子弹的编组
    bullets = Group() # 导入pygame.sprite中的Group类，创建一个Groyp实例，将其命名为bullets
    
    



    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        # 飞船位置在检测到键盘事件后（更新屏幕前）更新
        ship.update()

        bullets.update() # 将bullets传递给check_events和update_screen()
                         # 在check_events中，需要在玩家按空格处理bullets
                         # 对编组调用update时，编组自动对其中每个精灵调用update()，将为编组bullets中的每颗子弹调用bullet.update()

        # 删除已消失的子弹
        for bullet in bullets.copy():  # 不要从列表或编组中删除条目！！遍历编组的副本，使用copy来设置for循环，这样能使我们在循环中修改bullets
            if bullet.rect.bottom <= 0: # 检查这个编组中每颗子弹，看看是否已在屏幕顶端消失
                bullets.remove(bullet) # 消失就在编组中删掉这个子弹
        print(len(bullets)) # 显示当前还有多少子弹


        # 更新屏幕的图像
        gf.update_screen(ai_settings,screen,ship,bullets)# 在update_screen中，需要更新绘制到屏幕上的bullets
                         

run_game()