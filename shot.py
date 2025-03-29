import pygame
from circleshape import CircleShape
import constants

class Shot(CircleShape):
    def __init__(self, x, y, direction, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        # self.rotation = rotation
        self.direction = direction # Vector2()
        self.velocity = pygame.Vector2(0, 1)
        self.containers
        # print(f"Made shot at {x}, {y}: rot={self.direction}")

    def draw(self, screen):
        pygame.draw.circle( screen, "white", self.position, self.radius, 2)
        # print(f"Drawing asteroid at {self.position} with radius {self.radius}")

    def move( self, dt ):
        # forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += self.direction * constants.PLAYER_SHOOT_SPEED * dt

    def update(self, dt ):
        self.move(dt)
        # print(f"Moved to {self.x}, {self.y}")