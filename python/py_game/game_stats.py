class GameStats():
    """跟踪游戏的统计信息"""

    def _init_(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats() # 在_init_中调用他

    def reset_stats(self): # 初始化大部分统计信息
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
