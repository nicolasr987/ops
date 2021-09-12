import pygame
from pygame.locals import *
import fnmatch
pygame.init()
#inicializando
display = pygame.display.set_mode([800, 600])
pygame.display.set_caption("testi")
#tela
gameLoop = True
if __name__ == '__main__':
    print('funciona')
    #loop pra funcionar se n buga e para de funfar
    while gameLoop:
        display.fill([135, 0, 219])
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
             gameLoop = False
         elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_3:
                 print("oi")
        pygame.draw.rect(display, (200, 55, 55), (100, 220, 90, 60))

        pygame.display.update()

