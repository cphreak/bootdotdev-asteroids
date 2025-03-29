# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
import player

def main():
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    numpass, numfail = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_player = player.Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # print(f"dt= {dt}")
                return
        screen.fill((0,0,0))
        my_player.update(dt)
        my_player.draw(screen)
        pygame.display.flip()

        #end of loop
        dt = (clock.tick(60) / 1000 ) #convert millisecond to seconds

if __name__ == "__main__":
    main()