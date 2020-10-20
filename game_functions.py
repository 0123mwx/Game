import sys
import pygame
from bullet import Bullet


# KEYDOWN事件
def check_keydown_events(event, pw_settings, screen, ship, bullets):
    """响应按键"""

    # 如果按下的是右箭头键，就将ship.moving_right设置为True，从而将飞船向右移动
    if event.key == pygame.K_RIGHT:
        # 修改移动标志向右移动飞船
        ship.moving_right = True
    # 如果按下的是左箭头键，就将ship.moving_left设置为True，从而将飞船向左移动
    elif event.key == pygame.K_LEFT:
        # 修改移动标志向左移动飞船
        ship.moving_left = True
    # 如果按下的是空格键，就开火
    elif event.key == pygame.K_SPACE:
        # 创建新子弹，并将其加入到编组bullets中
        if len(bullets) < pw_settings.bullets_allowed:
            new_bullet = Bullet(pw_settings, screen, ship)
            bullets.add(new_bullet)


# KEYUP事件
def check_keyup_events(event, ship):
    """响应松开"""

    # 如果松开的是右箭头键，就将ship.moving_right设置为False，从而使飞船停止向右移动
    if event.key == pygame.K_RIGHT:
        # 修改移动标志停止向右移动飞船
        ship.moving_right = False
    # 如果松开的是左箭头键，就将ship.moving_left设置为False，从而使飞船停止向左移动
    elif event.key == pygame.K_LEFT:
        # 修改移动标志停止向左移动飞船
        ship.moving_left = False


def check_events(pw_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""

    for event in pygame.event.get():

        # 玩家单击游戏窗口的关闭按钮时，将检测到pygame.QUIT事件，此时调用sys.exit()来退出游戏
        if event.type == pygame.QUIT:
            sys.exit()

        # Pygame检测到KEYDOWN事件时作出响应
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, pw_settings, screen, ship, bullets)

        # Pygame检测到KEYUP事件时作出响应
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(pw_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""

    # 每次循环时都重绘屏幕
    screen.fill(pw_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()  # 绘制飞船

    # 让最近绘制的屏幕可见
    pygame.display.flip()
