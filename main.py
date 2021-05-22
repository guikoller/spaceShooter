import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")


WHITE = (255,255,255)

FPS = 60

SPACESHIP_HEIGHT, SPACESHIP_WIDHT = 40, 55

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDHT,SPACESHIP_HEIGHT)),90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDHT,SPACESHIP_HEIGHT)),-90)

BACKGROUND = pygame.image.load(os.path.join('Assets', 'space.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND,(WIDTH,HEIGHT))



def draw_window():
    WIN.blit(BACKGROUND, (0,0))
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (0,0))
    WIN.blit(RED_SPACESHIP_IMAGE,(300,300))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()