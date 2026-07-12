import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class Arsenal:
    def __init__(self, game:'AlienInvasion'):
        """Initialize the ship's arsenal."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()  # Group to hold all bullets fired by the ship

    def update_arsenal(self):
        """Update the position of bullets and remove old bullets."""
        self.arsenal.update()  # Update the position of each bullet
        self._remove_bullets_offscreen()  # Remove bullets that have moved off the screen

    def _remove_bullets_offscreen(self):
        """Remove bullets that have moved off the top of the screen."""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draw all bullets to the screen."""
        for bullet in self.arsenal.sprites():
            bullet.draw_bullet()

    def fire_bullet(self):
        """Fire a bullet if limit not reached yet."""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
    


       