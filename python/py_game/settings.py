class Settings():
    """存储外星人入侵的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""

        # 屏幕设置
        self.screen_width = 1200  # 窗口大小
        self.screen_height = 800  # 窗口大小
        self.bg_color = (230,230,230) # 窗口背景色

        # 飞船速度设置
        self.ship_speed_factor = 1.5 # 将速度值设置为小数值，更方便控制飞moving_right