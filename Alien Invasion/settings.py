class Settings:
    def __init__(self):
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship speed
        self.ship_speed = 2
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 1000

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
