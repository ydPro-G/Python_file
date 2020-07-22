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














# 添加射击功能，编写玩家按空格发射子弹的代码，子弹在屏幕中向上穿行，抵达屏幕边缘后消失




import sys
import pygame
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
    
    



    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ship)
        # 飞船位置在检测到键盘事件后（更新屏幕前）更新
        ship.update()
        # 更新屏幕的图像
        gf.update_screen(ai_settings,screen,ship)

run_game()