#-*- coding:utf-8 -*-
import pygame
from pygame.locals import *
white = 255,255,255
blue = 0,0,200
#初始化
pygame.init()
#创建窗口
screen = pygame.display.set_mode((600,500))
#创建文字对象
myfont = pygame.font.Font(None,60)
textImage = myfont.render("hello pygame",True,white)
pos_x = 300
pos_y = 250
vel_x = 2
vel_y = 1


while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            pygame.quit()


    screen.fill(blue)
    #screen.blit(textImage,(100,100))
    #pygame.draw.circle(screen, white, (300, 250), 100, 10)
    pos_x += vel_x
    pos_y += vel_y

    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x
    if pos_y  > 400 or pos_y < 0:
        vel_y = -vel_y
    pos = pos_x,pos_y,100,100
    pygame.draw.rect(screen,white,pos,0)
    pygame.display.update()
