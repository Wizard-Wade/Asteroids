from circleshape import CircleShape
from constants import *
import pygame
import pygame.freetype
import random



class Asteroid(CircleShape):
    anum = 0

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        self.name = f"A{Asteroid.anum}"
        Asteroid.anum += 1
    
    def draw(self, screen, font):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

        text_surface = font.render(self.name, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.position.x, self.position.y))
        screen.blit(text_surface, text_rect)

    def update(self, dt):
        self.position += self.velocity * dt
        

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        deflection = random.uniform(20, 50)
        split_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, split_radius)
        v1 = self.velocity.rotate(deflection)
        a1.velocity = v1 * 1.2
        
        a2 = Asteroid(self.position.x, self.position.y, split_radius)
        v2 = self.velocity.rotate(-deflection)
        a2.velocity = v2 * 1.2