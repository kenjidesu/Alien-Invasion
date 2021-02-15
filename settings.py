class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 668
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien Settings
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5
        
        self.easy = [0.5, 2.0, 0.5]
        self.medium = [0.9, 2.4, 0.8]
        self.hard = [1.1, 2.8, 1.0]
        self.levels = [self.easy, self.medium, self.hard]

        # Scoring
        self.alien_points = 50


    def initialize_dynamic_settings(self, level):
        """Initialize settings that change throughout the game"""
        self.ship_speed = self.levels[level][0]
        self.bullet_speed = self.levels[level][1]
        self.alien_speed = self.levels[level][2]

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1


    def increase_speed(self):
        """Increase speed settings and alien points values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        