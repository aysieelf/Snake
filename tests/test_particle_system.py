import unittest
from unittest.mock import Mock, patch

from src.effects.particle_system import ParticleSystem


def create_fake_particle(x, y, color):
    particle = Mock()
    particle.x = x
    particle.y = y
    particle.color = color
    return particle


class ParticleSystemShould(unittest.TestCase):
    def setUp(self):
        self.screen = Mock()
        self.particle_system = ParticleSystem(self.screen)

    def test_init_initializesSuccessfully(self):
        self.assertIsNotNone(self.particle_system)

    def test_init_setsScreen(self):
        self.assertEqual(self.screen, self.particle_system.screen)

    def test_init_setsParticles(self):
        self.assertEqual([], self.particle_system.particles)

    def test_init_setsNumParticles(self):
        self.assertEqual(10, self.particle_system.num_particles)

    def test_spawnParticles_addsParticlesToParticles(self):
        self.particle_system.spawn_particles(0, 0, (255, 255, 255))
        self.assertEqual(10, len(self.particle_system.particles))

    def test_update_removesDeadParticles(self):
        self.particle_system.particles = [Mock(), Mock(), Mock()]
        self.particle_system.particles[1].update.return_value = False
        self.particle_system.update()
        self.assertEqual(2, len(self.particle_system.particles))

    def test_draw_callsPygameDrawCircle(self):
        self.particle_system.particles = [
            create_fake_particle(0, 0, (255, 255, 255)),
            create_fake_particle(0, 0, (255, 255, 255)),
        ]
        with patch(
            "src.effects.particle_system.pygame.draw.circle"
        ) as mock_draw_circle:
            self.particle_system.draw()
            self.assertEqual(2, mock_draw_circle.call_count)
