import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        angle = random.uniform(20, 50)

        dir1 = self.velocity.rotate(angle)
        dir2 = self.velocity.rotate(angle * -1)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        spawn1 = Asteroid(self.position.x, self.position.y, new_radius)
        spawn2 = Asteroid(self.position.x, self.position.y, new_radius)

        spawn1.velocity = dir1 * 1.2
        spawn2.velocity = dir2 * 1.2