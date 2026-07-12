import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """A class to manage the ship."""
        
    def __init__(self, game: 'AlienInvasion', arsenal:'Arsenal'):

        """Initialize the ship and set its starting position."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        

        # Load the ship image and get its rect.
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_w, self.settings.ship_h)
            )

        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.boundaries.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)  # Store a decimal value for the ship's horizontal position
        self.arsenal = arsenal  # Reference to the ship's arsenal for firing bullets



    def update(self):
        """Update the ship's position based on movement flags."""
        #updating the position of the ship 
        self._update_ship_movement() 
        self.arsenal.update_arsenal()  # Update the position of bullets in the arsenal

    def _update_ship_movement(self):
        temp_speed = self.settings.ship_speed

        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x # Update rect object from self.x

    def draw(self):
        """Draw the ship at its current location."""
        self.arsenal.draw()  # Draw all bullets in the arsenal
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """Fire a bullet if limit not reached yet."""
        return self.arsenal.fire_bullet()
   