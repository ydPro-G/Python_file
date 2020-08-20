import pygame.font # 将文本渲染到屏幕上

class Button():

    def __init__(self,ai_settings,screen,msg):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen.rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width,self.height = 200, 50
        self.button_color = (0,250,0) 
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48) # 实参None让pygame使用默认字体，48是字号

        # 创建按钮的rect对象并使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center # 按钮的center属性为屏幕的center属性

        # 按钮标志只需要创建一次
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """将msg渲染为图像，并使其在按钮中居中"""
        self.msg_image = self.font.render(msg,True,self.text_color,
        self.button_color) # 将文本转化为图像，将图像存储在msg_image中，接受一个布尔实参，开启反锯齿功能

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center # 屏幕中央

    def draw_button(self):
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)