import pygame
from circleshape import CircleShape
from shot import Shot
import constants
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.containers
        self.shot_cooldown = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon( screen, "white", self.triangle(), 2)


    def rotate( self, dt ):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move( self, dt ):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += (forward * constants.PLAYER_SPEED * dt)
        # print(f"forward= {forward}")

    def shoot(self, dt):
        if (self.shot_cooldown > 0):
            return
        # print(f"Shot pos= {self.position}")
        x, y = self.position
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(x, y, direction, constants.SHOT_RADIUS)
        self.shot_cooldown = constants.PLAYER_SHOOT_COOLDOWN
        # forward = pygame.Vector2(0, 1).rotate(shot.rotation)
        # shot.position += forward * constants.PLAYER_SHOOT_SPEED * dt

    def update(self, dt):
        self.shot_cooldown -= dt
        keys = pygame.key.get_pressed()

# Rotate
        if keys[pygame.K_a]:
            self.rotate( (dt * -1 ))
        if keys[pygame.K_d]:
            self.rotate(dt)
# Move
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(( dt * -1 ))
# Shoot
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
