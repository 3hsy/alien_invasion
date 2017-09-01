__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import sys

import pygame

import game_functions

from setting import Setting
from ship import Ship


from pygame.sprite import Group

def run_game():
    pygame.init()
    ship_setting = Setting()
    screen = pygame.display.set_mode((ship_setting.screen_width, ship_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen,ship_setting)

    bullets = Group()
    aliens = Group()
    game_functions.creat_aliens(ship_setting,screen,aliens)

    while True:
        #
        game_functions.check(ship_setting,screen,ship,bullets)

        ship.update()
        game_functions.update_bullet(bullets,aliens)
        game_functions.upadte_alien(aliens)

       #更新背景#
        game_functions.update_screen(ship_setting, screen, ship, bullets, aliens)

run_game()
