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

        self.rect.centerx = self.rect.width
        self.rect.centery = self.rect.height

        self.x = float(self.rect.centerx)
        #飞船的左右上下移动
    def update(self,aliens):
        self.screen1 = self.screen.get_rect()
        for alien in aliens.sprites():
            if (alien.rect.right >= self.screen1.right or alien.rect.left < 0):
                for alien2 in aliens.sprites():
                    alien2.rect.y += self.ship_setting.aliendown_speed
                self.ship_setting.alien_direction *= -1
                break
        # 下面IF 这句要是不注释掉就100%有 bug，  注释掉后有时候上来是正常的，但是一旦发射子弹打掉任意一个飞船就会出现bug。
        #if (self.rect.right < self.screen1.right):
        self.x += self.ship_setting.alien_speed * self.ship_setting.alien_direction
        self.rect.x = self.x


    def blitme (self):
        self.screen.blit(self.image_alien, self.rect)

