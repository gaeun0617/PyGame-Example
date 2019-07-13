import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    logo = pygame.image.load("C:/Users/가은/Desktop/Ga-Eun/Python/PyGame-Example/pythonlogo.jpg")
    pos = [200,150]
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pos[0] -= 5
                elif event.key == K_RIGHT:
                    pos[0] += 5
                elif event.key == K_UP:
                    pos[1] -= 5
                elif event.key == K_DOWN:
                    pos[1] += 5

        pos[0] = pos[0] % 400
        pos[1] = pos[1] % 300

        rect = logo.get_rect()
        rect.center = pos
        SURFACE.blit(logo, rect)

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    main()