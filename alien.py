# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ship_setting,screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ship_setting = ship_setting
        self.image_alien = pygame.image.load('image/alien.jpg')
        self.rect = self.image_alien.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        # 飞船的左右上下移动

    def update(self):
        self.x += self.ship_setting.ALIEN_SPEED * self.ship_setting.ALIEN_DIRECTION
        self.rect.x = self.x

    def blitme (self):
        self.screen.blit(self.image_alien, self.rect)

