import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        split_vector1 = self.velocity.rotate(split_angle)
        split_vector2 = self.velocity.rotate(-split_angle)
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid1 = Asteroid(self.position.x, self.position.y, split_radius)
        split_asteroid2 = Asteroid(self.position.x, self.position.y, split_radius)
        split_asteroid1.velocity = split_vector1 * 1.8
        split_asteroid2.velocity = split_vector2
        self.kill()

        