#sansu asteroid game
import pygame, sys, os, random, math
from pygame.locals import *



pygame.init()
fps=pygame.time.Clock()



#colours
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
black=(0,0,0)



#global
width=800
height=600
time=0



#Home Screen
window=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('sansu asteroid')


#load images
#pygame.image.load('nokia.jpg')
#bg=pygame.image.load('images/nokia.jpg')
bg=pygame.image.load(os.path.join('images','background.jpg'))
deb=pygame.image.load(os.path.join('images','stone_bg.png'))
ship=pygame.image.load(os.path.join('images','ship.png'))

ship_x=width/2-50
ship_y=height/2-50
ship_angle=0
ship_is_rotating=False
ship_direction=0


def rot_center(image,angle):
    #rotates a surface ,maintaining a position
    orig_rect=image.get_rect()
    rot_image=pygame.transform.rotate(image,angle)
    rot_rect=orig_rect.copy()
    rot_rect.center=rot_image.get_rect().center
    rot_image=rot_image.subsurface(rot_rect).copy()
    return rot_image

#draw game func
def draw(canvas):
    global time
    canvas.fill(black)
    canvas.blit(bg,(0,0))
    canvas.blit(deb,(time*.3,0))
    canvas.blit(deb,(time*.3-width,0))
    time = time + 1
    canvas.blit(rot_center(ship,ship_angle),(ship_x,ship_y))

   
#(0,0)-Top left
#(width,0)-Top Right
#(0,hight)-Top Right
#(width,height)- right

#handle the inputs
def handle_input():
    global ship_angle,ship_is_rotating,ship_direction   
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==KEYDOWN:
            if event.key==K_LEFT:
                ship_is_rotating=True
                ship_direction=1

            elif event.key==K_RIGHT:
                ship_is_rotating=True
                ship_direction=0
        elif event.type==KEYUP:
            ship_is_rotating=False

                

    if ship_is_rotating:
        if ship_direction==0:
            ship_angle=ship_angle-1
        else:
            ship_angle=ship_angle+1



def update_screen():
    pygame.display.update()
    fps.tick(60)



while True:
    draw(window)
    handle_input()
    update_screen()
