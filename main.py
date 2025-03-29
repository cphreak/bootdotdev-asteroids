# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    numpass, numfail = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    Player.containers = (updatable, drawable,)
    Asteroid.containers = (updatable, drawable, asteroid, )
    AsteroidField.containers = (updatable, )
    my_field = AsteroidField()
    my_player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)
        for unit in asteroid:
            if (unit.collision(my_player)):
                print(f"Game over!")
                sys.exit()

        for unit in drawable:
            # print(unit)
            unit.draw(screen)

        pygame.display.flip()

        #end of loop
        dt = (clock.tick(60) / 1000 ) #convert millisecond to seconds

if __name__ == "__main__":
    main()