# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    numpass, numfail = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatables, drawables,)
    Shot.containers = ( updatables, drawables, shots )
    Asteroid.containers = (updatables, drawables, asteroids, )
    AsteroidField.containers = (updatables, )
    my_field = AsteroidField()
    my_player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatables.update(dt)
        for unit in asteroids:
            if (unit.collision(my_player)):
                print(f"Game over!")
                sys.exit()
            # print(f"Unit: {unit}")
            # else:
            for shot in shots:
                # print(f"Shot: {shot}")
                if (unit.collision(shot)):
                    shot.kill()
                    unit.kill()
                    print(f"Shot2Asteroid Collision!")

        for unit in drawables:
            # print(unit)
            unit.draw(screen)

        pygame.display.flip()

        #end of loop
        dt = (clock.tick(60) / 1000 ) #convert millisecond to seconds

if __name__ == "__main__":
    main()