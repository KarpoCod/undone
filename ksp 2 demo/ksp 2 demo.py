import pygame,random,sys,os

from pygame.locals import*

pygame.init()

mainClock = pygame.time.Clock()

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (255,255,255)
BACKGROUNDCOLOR = (0,0,0)

FPS = 60

STARMINSIZE = 10
STARMAXSIZE = 40
STARMINSPEED = 1
STARMAXSPEED = 6
ADDNEWSTARRATE = 6

PLAYERMOVERATE = 5



windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption("Kerbal Space Programm 2 demo")
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 35)

playerImage = pygame.image.load('rocket.png')
player = pygame.transform.scale(playerImage, (60, 60))
playerRect = pygame.Rect(200, 200, 60, 60)
starImage = pygame.image.load('star.png')

def terminate():
    pygame.quit()
    sys.exit

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
            return

def drawText(text, font, surface, x, y):
    textobj = font.render(text,1,TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

windowSurface.fill(BACKGROUNDCOLOR)
drawText('Космическая аркада', font, windowSurface, (WINDOWWIDTH/3), (WINDOWHEIGHT/3))
drawText('Нажмите клавишу для начала игры', font, windowSurface, (WINDOWWIDTH/3)-30, (WINDOWHEIGHT/3)+50)
pygame.display.update()
waitForPlayerToPressKey()

while True:
    stars = []
    starAddCounter = 0
    playerRect.topleft = (20, WINDOWHEIGHT/2)
    moveLeft = moveRight = moveUp = moveDown = False
    while True:
        windowSurface.fill(BACKGROUNDCOLOR)
        windowSurface.blit(player, playerRect)
        pygame.display.update()
        mainClock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == QUIT:
               terminate()

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()

                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False

                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False

                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
    
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False
    
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True

                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = True
                    moveLeft = False

                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True

                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = True
                    moveUp = False
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1*PLAYERMOVERATE,0)
        if moveRight and playerRect.left < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE,0)
        if moveUp and playerRect.left > 0:
            playerRect.move_ip(0, -1*PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)

        starAddCounter += 1
        if starAddCounter == ADDNEWSTARRATE:
            starAddCounter = 0



