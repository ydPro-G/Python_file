class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self,ai_settings): # 两个下划线
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats() # 在_init_中调用他
        # 游戏刚启动时处于非活跃状态
        self.game_active = False

    def reset_stats(self): # 初始化大部分统计信息
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
