class Settings():
    """a class to store all settings for alien invasion."""
    def __init__(self):
        # initialize the game's settings.
        # screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (93, 138, 168)

        # ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 13
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1