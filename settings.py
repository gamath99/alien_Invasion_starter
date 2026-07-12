import pathlib

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        self.name: str = "Alien Invasion"
        # Screen settings
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = pathlib.Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'