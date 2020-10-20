class Settings():
    """存储《飞机大战》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""

        # 屏幕设置
        """实参(1200, 800)是一个元组，指定了游戏窗口的尺寸。
        通过将这些尺寸值传递给pygame.display.set_mode()
        我们创建了一个宽1200像素、高800像素的游戏窗口"""
        self.screen_width = 1200
        self.screen_height = 800

        # 背景设置：设置背景色,默认为黑色，设置为浅灰色
        self.bg_color = (230, 230, 230)

        # 飞船设置：速度为1.5
        self.ship_speed_factor = 1.5

        # 子弹设置：这些设置创建宽3像素、高15像素的深灰色子弹。速度比飞船稍低。屏幕中数量最多为3。
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
