import sys

import pygame

def check_events(ship):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def check_keydown_events(event,ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings,screen,ship):
    """更新屏幕商的图像，并切换到新屏幕"""
    # 每次循环是都重绘屏幕
    screen.fill(ai_settings.bg_color);
    ship.bitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

