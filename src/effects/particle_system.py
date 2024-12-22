import pygame

from src.effects.particle import Particle


class ParticleSystem:
    def __init__(self, screen):
        self.screen = screen
        self.particles = []
        self.num_particles = 10

    def spawn_particles(self, x, y, color):
        for _ in range(self.num_particles):
            self.particles.append(Particle(x, y, color))


    def update(self):
        self.particles = [particle for particle in self.particles if particle.update()]

    def draw(self):
        for particle in self.particles:
            pygame.draw.circle(
                self.screen,
                particle.color,
                (int(particle.x), int(particle.y)),
                particle.size
            )