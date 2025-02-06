import pygame, sys, time
from pygame.locals import*
pygame.init()
windowSurface = pygame.display.set_mode((600,600), 0, 32)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
root=pygame.display.set_mode((600,600))
def drawtext(stroka):
    basicFont = pygame.font.SysFont(None,58)
    text = basicFont.render(stroka, True, BLACK)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery
    windowSurface.get_rect().centery
    windowSurface.fill(WHITE)
    windowSurface.blit(text, textRect)
    pygame.display.update()

drawtext('Ping pong')
pygame.display.update()
time.sleep(2)
player = pygame.Rect(300,500,80,30)
moveleft = False
moveRight = False
MOVESPEED = 25
a = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveleft = True
            if event.key ==K_RIGHT or event.key == K_d:
                moveleft = False
                moveRight = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                Pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveleft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
    if moveleft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < 600:
        player.right += MOVESPEED
    windowSurface.fill(WHITE)
    pygame.draw.rect(windowSurface,BLUE,player)
    pygame.display.update()
    time.sleep(0.05)
