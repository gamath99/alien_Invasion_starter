import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import Arsenal
#from alien import Alien
from alien_fleet import Alienfleet
from time import sleep
from button import Button
from hud import HUD

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()

        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

        self.game_stats = GameStats(self)
        self.HUD = HUD(self)
        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()  # Initialize the mixer module for sound
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)  # Load the laser sound
        self.laser_sound.set_volume(0.7)  # Set the volume for the laser sound

        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)  # Load the impact sound
        self.impact_sound.set_volume(0.7)  # Set the volume for the impact sound

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet =Alienfleet(self)  # Create an instance of the Alienfleet class
        self.alien_fleet.create_fleet()  # Create the initial fleet of aliens

        self.play_button = Button(self, 'Play')
        self.game_active = False
                
    def run_game(self):
        """Start the main loop for the game."""
        # Game loop 
        while self.running:
            # Watch for keyboard and mouse events.
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()  # Update the alien's position
                self._check_collisions()            
            # Make the most recently drawn screen visible.
            self._update_screen()
            self.clock.tick(self.settings.FPS) 

    def _check_collisions(self):
        #check collision for ship 
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status() 
            # the ship to recenter
            # subtract one life if possible 

         #check collisions for alien and bottom of screen
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()

        #check collisions of projectiles and aliens 
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()    
            self.impact_sound.fadeout(500)
            self.game_stats.update(collisions)
            self.HUD.update_scores()

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            # Update game stats level
            self.game_stats.update_level()
            # Update HUD view 

    
    def _check_game_status(self):
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False


        print(self.game_stats.ships_left)
        
   
      
    
    def _reset_level(self):
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()


    def restart_game(self):
        self.settings.initialize_dynamic_settings()    
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible (False)

    
    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        self.alien_fleet.draw()  # Draw all aliens in the fleet
        self.HUD.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_stats.save_scores()
                pygame.quit()
                sys.exit() # Limit the frame rate to 60 FPS
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()
             

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
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                # play the laser sound
                self.laser_sound.play()    
                self.laser_sound.fadeout(250)  # Fade out the sound after 250 milliseconds

        elif event.key == pygame.K_q:
            self.running = False
            self.game_stats.save_scores()
            pygame.quit()
            sys.exit() # Limit the frame rate to 60 FPS           
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
