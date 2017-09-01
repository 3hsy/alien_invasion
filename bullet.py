__author__ = 'Administrator'
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ship_setting,screen,ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.image_bullet = pygame.image.load('image/bullet.jpg')
        self.rect = self.image_bullet.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.bullet_speed = ship_setting.bullet_speed
        self.middle2 = float(self.rect.y)

    def update(self):
        self.middle2 -= self.bullet_speed
        self.rect.y = self.middle2
    def blitme(self):
        self.screen.blit(self.image_bullet , self.rect)



