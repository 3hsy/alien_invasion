# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import sys

import pygame

import game_functions

import setting
from ship import Ship


from pygame.sprite import Group

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((setting.SCREEN_WIDTH, setting.SCREEN_HEIGHT))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen,setting)

    bullets = Group()
    aliens = Group()
    game_functions.creat_aliens(setting,screen,aliens)

    while True:
        #
        game_functions.check(setting,screen,ship,bullets)

        ship.update()
        game_functions.update_bullet(bullets,aliens)
        game_functions.upadte_aliens(aliens)

       #更新背景#
        game_functions.update_screen(setting, screen, ship, bullets, aliens)

run_game()
