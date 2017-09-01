__author__ = 'Administrator'

import pygame

class Ship():
    def __init__(self,screen,setting):
        #������ʼλ��
        self.screen = screen
        self.image = pygame.image.load('image/ship.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #���ó�ʼmark
        self.moving_mark = False
        self.moving_mark2 = False
        #setting����
        self.ship_setting = setting
        #�����м��������ڽ���С��
        self.middle =float(self.rect.centerx)
    def update(self):
        #���������ı仯
        if self.moving_mark and self.rect.right < self.screen_rect.right :
            self.middle += self.ship_setting.ship_speed
        if self.moving_mark2 and self.rect.left > 0:
            self.middle -= self.ship_setting.ship_speed
        self.rect.centerx = self.middle
    def blitme(self):
        self.screen.blit(self.image , self.rect)
