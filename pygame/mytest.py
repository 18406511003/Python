# __author__ = 'Toooooooo'
# -*- coding: utf-8 -*-

# import pygame
# from pygame.locals import *
# from sys import exit
#
# pygame.init()
# screen = pygame.display.set_mode((640,480),0,32)
#
# import pygame
# from pygame.locals import *
# from sys import exit
#
# pygame.init()
#
# screen = pygame.display.set_mode((640, 480), 0, 32)
# screen.fill([255,255,255])
# # surface1 = pygame.surface.Surface((640, 80))
# def New_s(height):
#     red_surface = pygame.surface.Surface((640,height))
#     green_surface = pygame.surface.Surface((640,height))
#     blue_surface = pygame.surface.Surface((640,height))
#     for x in range(640):
#         c = int((x/640.)*255)
#         red=(c,0,0)
#         green=(0,c,0)
#         blue=(0,0,c)
#         line_rect = Rect(x, 0, 1, height)
#         pygame.draw.rect(red_surface,red,line_rect)
#         pygame.draw.rect(green_surface,green,line_rect)
#         pygame.draw.rect(blue_surface,blue,line_rect)
#     return red_surface,green_surface,blue_surface
#
# red,green,blue=New_s(80)
# color=[127,0,0]
#
# # pygame.display.set_caption("Hello, World!")
# # back1=pygame.draw.rect(screen,[255,70,90],[0,0,640,80])
# # back2=pygame.draw.rect(screen,[255,0,80],[0,80,640,80])
# # back3=pygame.draw.rect(screen,[0,0,100],[0,160,640,80])
# # pygame.draw.circle(screen,[255,255,255],[320,40],30)
# # # pygame.draw.rect(在什么表面、颜色、位置（left,top,width,height）)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             exit()
#     # screen.blit(surface1,(200,200))
#
#     screen.blit(red, (0, 00))
#     screen.blit(green, (0, 80))
#     screen.blit(blue, (0, 160))
#
#     x, y = pygame.mouse.get_pos()
#
#     if pygame.mouse.get_pressed()[0]:
#         for a in range(3):
#             if y>a*80 and y<(a +1)*80:
#                 color[a]=int((x /639.)*255.)
#                 print color[a]
#         pygame.display.set_caption(str(tuple(color)))
#     # for component in range(3):
#     #     pos = ( int((color[component]/255.)*639), component*80+40 )
#     #     pygame.draw.circle(screen, (255, 255, 255), pos, 20)
#     #
#     # pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240))
#     for a in range(3):
#         print color[a]
#         pos = ( int((color[a]/255.) * 639), a *80+40)
#         pygame.draw.circle(screen,(255,255,255),pos,20)
#     pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240))
#
#     pygame.display.update()
#     # x, y = pygame.mouse.get_pos()
#     # if pygame.mouse.get_pressed()[0]:
#     #     for component in range(3):
#     #         if y > component*80 and y < (component+1)*80:
#     #             color[component] = int((x/639.)*255.)
#     #     pygame.display.set_caption("PyGame Color Test - "+str(tuple(color)))


# import pygame
# from pygame.locals import *
# from sys import exit
# from gameobjects.vector2 import Vector2
#
# pygame.init()
# screen = pygame.display.set_mode((640,480),0,32)
# screen.fill([255,255,255])
# car = pygame.image.load("ok1.jpg").convert()
#
# # pygame.init()
# #
# # screen = pygame.display.set_mode((640, 480), 0, 32)
# #
# # background = pygame.image.load(background_image_filename).convert()
# # sprite = pygame.image.load(sprite_image_filename).convert_alpha()
# #
# # clock = pygame.time.Clock()
# #
# # sprite_pos = Vector2(200, 150)
# # sprite_speed = 300.
# pos=[320,480]
#
# while True:
#
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             exit()
#         elif event.type == pygame.KEYDOWN:
#
#                 if event.key==pygame.K_UP:
#                     pos[1]=pos[1]-50
#                     print pos[1]
#                     # if looper<-480:
#                     #    looper=480
#                     pygame.draw.rect(screen,[255,255,255],[pos[0],(pos[1]+132),83,132],0)
#                     screen.blit(car,tuple(pos))
#                 if event.key==pygame.K_DOWN:
#                     pos[1]+=50
#                     # if looper>480:
#                     #    looper=-480
#                     pygame.draw.rect(screen,[255,255,255],[pos[0],(pos[1]-132),83,132],0)
#                     screen.blit(car,tuple(pos))
#                 if event.key==pygame.K_LEFT:
#                     pos[0]-=50
#                     pygame.draw.rect(screen,[252,255,255],[pos[0]+50,pos[1],83,132],0)
#                     screen.blit(car,pos)
#                 if event.key==pygame.K_RIGHT:
#                     pos[0]+=50
#                     pygame.draw.rect(screen,[252,255,255],[pos[0]-50,pos[1],83,132],0)
#                     screen.blit(car,pos)
#     my_font=pygame.font.SysFont(None,22)
#     textstr='location:'+str(pos[0])+','+str(pos[1])
#     text_screen=my_font.render(textstr, True, (255, 0, 0))
#     screen.blit(text_screen, (50,50))
#     pygame.display.update()

import pygame,sys,os,random
pygame.init()

class rect():#画出小人
    def __init__(self,filename,initial_position):
        self.image=pygame.image.load(filename)
        self.rect=self.image.get_rect()
        self.rect.topleft=initial_position

class goldrect(pygame.sprite.Sprite):#绘出金币
    def __init__(self,gold_position,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('gold.png')
        self.rect=self.image.get_rect()
        self.rect.topleft=gold_position
        self.speed=speed
    def move(self):
        self.rect=self.rect.move(self.speed)

def drawback(): #绘出背景图片
    my_back=pygame.image.load('qi3.jpg')
    bakscreen.blit(my_back,[0,0])


def loadtext(levelnum,score,highscore):#绘出成绩、level、最高分等
    my_font=pygame.font.SysFont(None,24)
    levelstr='Level:'+str(levelnum)
    text_screen=my_font.render(levelstr, True, (255, 0, 0))
    bakscreen.blit(text_screen, (650,50))
    highscorestr='Higescore:'+str(highscore)
    text_screen=my_font.render(highscorestr, True, (255, 0, 0))
    bakscreen.blit(text_screen, (650,80))
    scorestr='Score:'+str(score)
    text_screen=my_font.render(scorestr, True, (255, 0, 0))
    bakscreen.blit(text_screen, (650,110))

def loadgameover(scorenum,highscore):#绘出GAME OVER
    my_font=pygame.font.SysFont(None,50)
    levelstr='GAME OVER'
    over_screen=my_font.render(levelstr, True, (255, 0, 0))
    bakscreen.blit(over_screen, (300,240))
    highscorestr='YOUR SCORE IS '+str(scorenum)
    over_screen=my_font.render(highscorestr, True, (255, 0, 0))
    bakscreen.blit(over_screen, (280,290))
    if scorenum>int(highscore):#写入最高分
        highscorestr='YOUR HAVE GOT THE HIGHEST SCORE!'
        text_screen=my_font.render(highscorestr, True, (255, 0, 0))
        bakscreen.blit(text_screen, (100,340))
        highfile=open('highscore','w')
        highfile.writelines(str(scorenum))
        highfile.close()

def gethighscore(): #读取最高分
    if os.path.isfile('highscore'):
        highfile=open('highscore','r')
        highscore=highfile.readline()
        highfile.close()
    else:
        highscore=0
    return highscore

bakscreen=pygame.display.set_mode([800,600])
bakscreen.fill([0,160,233])
pygame.display.set_caption('Dig!Dig!')
drawback()

levelnum=1 #level
scorenum=0 #得分
highscore=gethighscore()#最高分
ileft=1  #记录向左移动步数，用来控制图片
iright=10 #记录向右移动步数，用来控制图片
x=100
y=450
filename='1.png'
backimg_ren=rect(filename,[x,y])
bakscreen.blit(backimg_ren.image,backimg_ren.rect)
loadtext(levelnum,scorenum,highscore)
goldx=random.randint(50,580)
speed=[0,levelnum*8]
mygold=goldrect([goldx,100],speed)
pygame.display.update()
while True:
    if scorenum>0 and scorenum/50.0==int(scorenum/50.0):#当得分是50的倍数时修改level
        levelnum=scorenum/50+1
        speed=[0,levelnum*100]

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    #make gold

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:#按下左键

        drawback()
        loadtext(levelnum,scorenum,highscore)

        if iright > 14 :iright=10
        iright=iright+1
        filename=str(iright)+'.png'
        if x<50 :
            x=50
        else:
            x=x-10

        backimg_surface=rect(filename,[x,y])
        bakscreen.blit(backimg_surface.image,backimg_surface.rect)


    if pressed_keys[pygame.K_RIGHT]:#按下右键

        drawback()
        loadtext(levelnum,scorenum,highscore)

        if ileft > 4 :ileft=0
        ileft=ileft+1
        filename=str(ileft)+'.png'
        if x>560:
            x=560
        else:
            x=x+10

        backimg_surface=rect(filename,[x,y])
        bakscreen.blit(backimg_surface.image,backimg_surface.rect)

    drawback()
    loadtext(levelnum,scorenum,highscore)
    mygold.move()
    bakscreen.blit(mygold.image,mygold.rect)

    backimg_surface=rect(filename,[x,y])
    bakscreen.blit(backimg_surface.image,backimg_surface.rect)
    if mygold.rect.top>600:#判断金币是否着地
        loadgameover(scorenum,highscore)
    if mygold.rect.colliderect(backimg_surface.rect):#判断金币是否与小人碰撞
        scorenum+=5
        loadtext(levelnum,scorenum,highscore)
        goldx=random.randint(50,580)
        mygold=goldrect([goldx,100],speed)
    pygame.display.update()