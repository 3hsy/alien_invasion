__author__ = 'Administrator'
import sys

import pygame
from bullet import Bullet
from alien import Alien
from random import randint

def check(ship_setting,screen,ship,bullets):
    for event in pygame.event.get():
        #检查退出
            if pygame.QUIT == event.type:
                sys.exit()
        #检查按键，设置mark值
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:

                    ship.rect.centerx += 100
                    ship.moving_mark = True
                if event.key == pygame.K_LEFT:
                    ship.rect.centerx -= 100
                    ship.moving_mark2 = True
                #发射
                if event.key ==pygame.K_SPACE:
                    if len(bullets) <= ship_setting.bullet_allow:
                        new_bullet = Bullet(ship_setting,screen,ship)
                        bullets.add(new_bullet)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_mark = False
                if event.key == pygame.K_LEFT:
                    ship.moving_mark2 = False

#创建外星飞船
def creat_aliens(ship_setting, screen, aliens):
    alien = Alien(ship_setting, screen)

    number_count = int((ship_setting.screen_height - alien.rect.height *9 ) / (alien.rect.height))
    for number in range(number_count):
         distance = alien.rect.width
         while( distance < (ship_setting.screen_width - alien.rect.width * 5) ):
            randomnumber = randint (1,3)
            distance += randomnumber  * alien.rect.width
            alien = Alien(ship_setting, screen)
            alien.x = distance
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height * number*2 + alien.rect.height
            aliens.add(alien)
#更新飞船
def update_screen(ai_setting, screen, ship,bullets,aliens):
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    #这句不知道为什么不对
    # aliens.draw(screen)
    for alien in aliens.sprites():
        alien.blitme()
    for bullet in bullets.sprites():
        bullet.blitme()

    pygame.display.flip()
def upadte_alien(aliens):
    aliens.update(aliens)

def update_bullet(bullets, aliens):
     bullets.update()
     for bullet in bullets.copy():
          if bullet.rect.bottom <= 0:
              bullets.remove(bullet)
     boom=pygame.sprite.groupcollide(bullets, aliens, True, True )

