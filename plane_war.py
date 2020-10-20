import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象：初始化背景设置,让Pygame能够正确地工作
    pygame.init()

    pw_settings = Settings()

    """调用pygame.display.set_mode()来创建一个名为screen的显示窗口，
    这个游戏的所有图形元素都将在其中绘制。每个元素（如外星人或飞船）都是一个surface对象"""
    screen = pygame.display.set_mode((pw_settings.screen_width, pw_settings.screen_height))

    # 窗口标题
    pygame.display.set_caption('Plane War')

    # 创建一艘飞船
    ship = Ship(pw_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        gf.check_events(pw_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # 删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(pw_settings, screen, ship, bullets)


run_game()
