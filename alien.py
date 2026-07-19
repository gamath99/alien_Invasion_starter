import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_Invasion_starter.alien_fleet import AlienFleet

class Alien(Sprite):
    """A class to manage aliens in the game."""
    
    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        """Create an alien object at the top of the screen."""
        super().__init__()              
                
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.alien_w, self.settings.alien_h)
            )

        # Create an alien rect at (0, 0) and then set correct position.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        
        # Store the alien's position as a decimal value.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen."""
        temp_speed = self.settings.fleet_speed

        if self.check_edges():
            self.settings.fleet_direction *= -1
            self.y +=self.settings.fleet_drop_speed

        self.x += temp_speed * self.settings.fleet_direction
        self.rect.x = self.x  # Update the rect position.
        self.rect.y = self.y  # Update the rect position.

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        return(self.rect.right >= self.boundaries.right or self.rect.left <= 0
            )
        if self.rect.right >= self.boundaries.right or self.rect.left <= 0:
            return True
        return False


       

    def draw_alien(self):
        """Draw the alien to the screen."""
        self.screen.blit(self.image, self.rect)