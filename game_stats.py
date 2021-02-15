class GameStats:
    """Track statistics for Alien Invaion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an active state
        self.game_active = False

        # Read high score from the file
        with open('high_score.txt') as file:
            previous_score = file.read()
        self.high_score = int(previous_score)

    
    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1