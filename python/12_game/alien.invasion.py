import sys
import pygame     #引入pygame
def run_game():   #定义一个运行游戏界面的界面
    #初始化游戏并且创建一个屏幕对象
    pygame.init()   #初始化pygame背景设置
    screen=pygame.display.set_mode((1200,800))  #设置pygame窗口尺寸的分别率 1200*800
    pygame.display.set_caption("Alien Invasion") #游戏运行窗口的标题

    # 创建一种背景色，并将其存储在bg_color中，我们需要在while循环前定义它
    bg_color = (230,230,230)

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    sys.exit()
                except SystemExit as msg:
                    break
        
        # 每次循环时都重绘屏幕，调用方法screenfill()，用背景色填充屏幕，这个方法只接受一个实参，一种颜色        screen.fill(bg_color)


        # 让最近绘制的屏幕可见
        pygame.display.flip()  

run_game()






