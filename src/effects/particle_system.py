from src.effects.particle import Particle

import pygame


class ParticleSystem:
    """
    A simple particle system class that manages a collection of particles.
    """

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.particles: list = []
        self.num_particles: int = 10

    def spawn_particles(self, x: int, y: int, color: tuple) -> None:
        """
        Spawn a collection of particles at the given position.

        Args:
            x (int): The x-coordinate of the spawn position.
            y (int): The y-coordinate of the spawn position.
            color (tuple): The color of the particles.
        """
        for _ in range(self.num_particles):
            self.particles.append(Particle(x, y, color))

    def update(self) -> None:
        """
        Update the particles in the system.
        Remove particles that are no longer alive.
        """
        self.particles = [particle for particle in self.particles if particle.update()]

    def draw(self) -> None:
        """
        Draw the particles on the screen.
        """
        for particle in self.particles:
            pygame.draw.circle(
                self.screen,
                particle.color,
                (int(particle.x), int(particle.y)),
                particle.size,
            )
