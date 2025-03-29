import random
import pygame
from circleshape import CircleShape
import constants

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.rotation = 0
        self.containers
        # print(f"Made a asteroid at {x}, {y}")

    def draw(self, screen):
        pygame.draw.circle( screen, "white", self.position, self.radius, 2)
        # print(f"Drawing asteroid at {self.position} with radius {self.radius}")

    def move( self, dt ):
        # forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += self.velocity * dt

    def update(self, dt ):
        self.move(dt)
        # print(f"Moved to {self.x}, {self.y}")

    def split(self):
        self.kill()
        if (self.radius <= constants.ASTEROID_MIN_RADIUS):
            return
        x, y = self.position
        angle = random.uniform(20, 50)
        self.radius -= constants.ASTEROID_MIN_RADIUS
        asteroid = Asteroid( x, y, self.radius)
        # asteroid.velocity = pygame.Vector2(0, 1).rotate(self.rotation + angle)
        asteroid.velocity = self.velocity.rotate(self.rotation + angle) * constants.ASTEROID_SPLIT_SPEED
        asteroid = Asteroid( x, y, self.radius)
        asteroid.velocity = self.velocity.rotate(self.rotation - angle) * constants.ASTEROID_SPLIT_SPEED
