import sys
import random
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        SURFACE.fill((0,0,0))

        pointList = []
        for _ in range(10):
            xpos = random.randint(0, 400)
            ypos = random.randint(0, 300)
            pointList.append((xpos,ypos))
        
        pygame.draw.lines(SURFACE, (255,255,255), True, pointList, 5)

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == "__main__":
    main()