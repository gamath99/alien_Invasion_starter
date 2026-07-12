import sys
import pygame
from settings import Settings

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
        
    def run_game(self):
        """Start the main loop for the game."""
        while self.running:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            # Make the most recently drawn screen visible.
            self.screen.blit(self.bg, (0, 0))
            pygame.display.flip()
            self.clock.tick(self.settings.FPS)  # Limit the frame rate to 60 FPS
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
