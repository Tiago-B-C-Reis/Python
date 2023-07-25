class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080

        # RGB colors: a mix of red, green, and blue (255, 255, 255):
        self.bg_color = (20, 20, 180)

        # Bullets limit:
        self.bullets_allowed = 5

        # This setting allow to choose from different backgrounds
        self.bg_choice = 1

        # Limit of ships that can be used before losing:
        self.ship_limit = 3

        # Bullets settings:
        self.bullet_width = 6
        self.bullet_height = 20
        self.bullet_color = (250, 0, 0)

        # Alien settings:
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right; -1 represents left:
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2
        self.alien_speed = 1
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50
        self.alien_2_points = 50
        self.alien_3_points = 500
        self.alien_4_points = 10000

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)




