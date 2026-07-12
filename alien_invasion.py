import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

        self.running = True
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        
    def run_game(self):
        """Start the main loop for the game."""
        while self.running:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            # Make the most recently drawn screen visible.
            self._update_screen()
            self.clock.tick(self.settings.FPS) 

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit() # Limit the frame rate to 60 FPS
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
             

    def _check_keyup_events(self, event):
        pass
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
       
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit() # Limit the frame rate to 60 FPS           
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
