import pygame


class SoundEffects:
    """Manage sound effects of the game"""

    def __init__(self):
        """Load Sound Effects"""
        self.beam = pygame.mixer.Sound('sounds/laser.wav')
        self.explosion = pygame.mixer.Sound('sounds/explosion.wav')
        self.game_over = pygame.mixer.Sound('sounds/houston.wav')
        self.alien_effect = pygame.mixer.Sound('sounds/growl1.wav')
        self.alien_explode = pygame.mixer.Sound('sounds/alienExplode.wav')


    def bg_music(self):
        """Background Music of the game"""
        pygame.mixer.music.load('sounds/interstellar.wav')
        pygame.mixer.music.play(-1)