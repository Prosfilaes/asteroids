import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print ("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for u in updatable:
            u.update(dt)
        screen.fill ((0, 0, 0))
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(FPS) / 1000 # convert from milliseconds to seconds

if __name__ == "__main__":
    main()
