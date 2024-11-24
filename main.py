import pygame
from constants import *
from player import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import sys

def main():
    pygame.init()
    print ("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField ()

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            if a.isCollision(player):
                print ("Game over!")
                sys.exit(0)
            for s in shots:
                if a.isCollision(s):
                    a.split()
                    s.kill()
        screen.fill ((0, 0, 0))
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(FPS) / 1000 # convert from milliseconds to seconds

if __name__ == "__main__":
    main()
