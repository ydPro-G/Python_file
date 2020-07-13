# 一个settings模块，包含一个settings类
# 将所有设置存储在一个地方
# 这样我们就能传递一个设置对象


class Settings():
    """存储{外星人入侵}的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_winth = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)