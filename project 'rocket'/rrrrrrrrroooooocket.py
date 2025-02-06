import pygame, random, sys
from pygame.locals import*
pygame.init()
mainClock = pygame.time.Clock()
WINWIDTH = 600
WINHEIGHT = 600
TEXTCOLOR = (225,230,155)
BGCOLOR=(0,0,0)
FPS = 60
STARMINSIZE = 10
STARMAXSIZE = 40
STARMINSPEED = 1
STARMAXSPEED = 6
ADDNEWSTARRATE = 6
PLAYERMOVERATE = 5

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return

def drawText(text,font,surface,x,y):
    textobj = font.render(text,1,TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)
windowSurface = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption('need 4 space')
pygame.mouse.set_visible(False)
font = pygame.font.SysFont(None,35)
playerImage = pygame.image.load('rocket.png')
player = pygame.transform.scale(playerImage,(60,60))
playerRect = pygame.Rect(200,200,60,60)
starImage = pygame.image.load('star.png')
windowSurface.fill(BGCOLOR)
drawText('AHTUNG!',font,windowSurface,(WINWIDTH/3),(WINHEIGHT/3))
drawText("cdelai chto-nibud'", font,windowSurface,(WINWIDTH/3)-30,(WINHEIGHT/3)+50)
pygame.display.update()
waitForPlayerToPressKey()
while True:
    playerRect.topleft = (20,WINHEIGHT/2)
    moveLeft = moveRight = moveUp = moveDown = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
        windowSurface.fill(BGCOLOR)
        windowSurface.blit(player,playerRect)
        pygame.display.update()
        mainClock.tick(FPS)
