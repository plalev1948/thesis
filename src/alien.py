import os
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Get the directory path of the current script file.
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Load the alien image and set its rect attribute.
        image_path = os.path.join(current_dir, 'images', 'alien3.bmp')
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
      """Return True if alien is at edge of screen."""
      screen_rect = self.screen.get_rect()
      if self.rect.right >= screen_rect.right or self.rect.left <= 0:
          return True
      return False
        
    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x