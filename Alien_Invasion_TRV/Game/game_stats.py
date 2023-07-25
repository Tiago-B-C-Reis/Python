import json


class GameStats:
    """Track statistics for ALien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start ALien Invasion in an active state:
        self.game_active = False

        # High score should is stored, is order to not be changed,
        # unless there is a new high score.
        filename = '../high_score_memory.json'
        with open(filename) as f:
            self.high_score = json.load(f)

        self.get_stored_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def get_stored_high_score(self):
        """Get stored high_score if available."""
        filename = '../high_score_memory.json'
        try:
            with open(filename) as f:
                high_score = json.load(f)
        except FileNotFoundError:
            return None
        else:
            if high_score < self.high_score:
                self.store_new_high_score()

    def store_new_high_score(self):
        """Prompt for a new username."""
        high_score = self.high_score
        filename = '../high_score_memory.json'
        with open(filename, 'w') as f:
            json.dump(high_score, f)
        return high_score

