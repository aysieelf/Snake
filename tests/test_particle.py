import unittest

from src.effects.particle import Particle


class ParticleShould(unittest.TestCase):
    def setUp(self):
        self.particle = Particle(0, 0, (255, 255, 255))

    def test_init_initializesSuccessfully(self):
        self.assertIsNotNone(self.particle)

    def test_init_setsX(self):
        self.assertEqual(0, self.particle.x)

    def test_init_setsY(self):
        self.assertEqual(0, self.particle.y)

    def test_init_setsVelocityX(self):
        self.assertIsNotNone(self.particle.velocity_x)

    def test_init_setsVelocityY(self):
        self.assertIsNotNone(self.particle.velocity_y)

    def test_init_setsLifetime(self):
        self.assertIsNotNone(self.particle.lifetime)

    def test_init_setsInitialLifetime(self):
        self.assertIsNotNone(self.particle.initial_lifetime)

    def test_init_setsColor(self):
        self.assertEqual((255, 255, 255), self.particle.color)

    def test_init_setsSize(self):
        self.assertEqual(2, self.particle.size)

    def test_update_returnsFalse_whenLifetimeZero(self):
        self.particle.lifetime = 0

        result = self.particle.update()

        self.assertFalse(result)

    def test_update_decreasesLifetime(self):
        self.particle.lifetime = 10

        self.particle.update()

        self.assertEqual(9, self.particle.lifetime)

    def test_update_changesColorAlpha(self):
        self.particle.lifetime = 10
        self.particle.initial_lifetime = 10

        self.particle.update()

        self.assertEqual((255, 255, 255, 229), self.particle.color)

    def test_update_movesParticle(self):
        self.particle.x = 0
        self.particle.y = 0

        self.particle.update()

        self.assertNotEqual(0, self.particle.x)
        self.assertNotEqual(0, self.particle.y)

    def test_update_returnsTrue_whenLifetimePositive(self):
        self.particle.lifetime = 10

        result = self.particle.update()

        self.assertTrue(result)
