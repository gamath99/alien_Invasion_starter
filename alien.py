import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    """A class to manage aliens in the game."""
    
    def __init__(self, game: 'AlienInvasion', x:float, y:float):
        """Create an alien object at the top of the screen."""
        super().__init__()              
        self.game = game 
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.alien_w, self.settings.alien_h)
            )

        # Create an alien rect at (0, 0) and then set correct position.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        
        # Store the alien's position as a decimal value.
       #self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        pass

    def draw_alien(self):
        """Draw the alien to the screen."""
        self.screen.blit(self.image, self.rect)