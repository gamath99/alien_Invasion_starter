import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class Alienfleet:
    """A class to manage the alien fleet."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the alien fleet."""
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()  # Group to hold all alien sprites
        self.fleet_direction = self.settings.fleet_direction  
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()  # Create the initial fleet of aliens
        

    def create_fleet(self):
        """Create a full fleet of aliens."""
        alien_w = self.settings.alien_w
        screen_w = self.settings.screen_w

        fleet_w = self.calculate_fleet_size(alien_w, screen_w)

        fleet_horizontal_space = fleet_w * alien_w
        x_offset = int((screen_w - fleet_horizontal_space) // 2)  # Center the fleet horizontally

        for col in range(fleet_w):
            current_x = alien_w * col + x_offset
            if col % 2 == 0:
                continue
            self._create_alien(current_x, 10)

           
    def calculate_fleet_size(self, alien_w, screen_w):
        fleet_w = (screen_w // alien_w)
        
        if fleet_w % 2 == 0:
            fleet_w -= 1  # Ensure an odd number of aliens for symmetry
        else:
            fleet_w -= 2  # Adjust to ensure symmetry
        return fleet_w

    def _create_alien(self, current_x:int, current_y:int):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)  # Add the new alien to the fleet group
    
    def draw(self):
        """Draw all aliens in the fleet."""
        alien:'Alien'
        for alien in self.fleet:
            alien.draw_alien()  # Call the draw method for each alien



