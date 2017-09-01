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
        #�ɴ������������ƶ�
    def update(self,aliens):
        self.screen1 = self.screen.get_rect()
        for alien in aliens.sprites():
            if (alien.rect.right >= self.screen1.right or alien.rect.left < 0):
                for alien2 in aliens.sprites():
                    alien2.rect.y += self.ship_setting.aliendown_speed
                self.ship_setting.alien_direction *= -1
                break
        # ����IF ���Ҫ�ǲ�ע�͵���100%�� bug��  ע�͵�����ʱ�������������ģ�����һ�������ӵ��������һ���ɴ��ͻ����bug��
        #if (self.rect.right < self.screen1.right):
        self.x += self.ship_setting.alien_speed * self.ship_setting.alien_direction
        self.rect.x = self.x


    def blitme (self):
        self.screen.blit(self.image_alien, self.rect)

