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
deb=pygame.image.load(os.path.join('images','ship.png'))


#draw game func
def draw(canvas):
    global time
    canvas.fill(black)
    canvas.blit(bg,(0,0))
    canvas.blit(deb,(time*.3,0))
    canvas.blit(deb,(time*.3-width,0))
    time = time + 5

    

#handle the inputs
def handle_input():
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()


def update_screen():
    pygame.display.update()
    fps.tick(60)



while True:
    draw(window)
    handle_input()
    update_screen()
