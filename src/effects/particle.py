from random import randint, uniform


class Particle:
    """
    A simple particle class that represents a single particle in the particle system.
    """

    def __init__(self, x: int, y: int, color: tuple):
        self.x = x
        self.y = y
        self.velocity_x = uniform(-2, 2)
        self.velocity_y = uniform(-2, 2)
        self.lifetime = randint(30, 60)
        self.initial_lifetime = self.lifetime
        self.color = color
        self.size = 2

    def update(self) -> bool:
        """
        Update the particle's position and lifetime.

        Returns:
            bool: True if the particle is still alive, False otherwise.
        """
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.lifetime -= 1

        alpha = int((self.lifetime / self.initial_lifetime) * 255)
        self.color = (*self.color[:3], alpha)

        return self.lifetime > 0
