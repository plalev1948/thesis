import os
import pygame

class Ship:
    """A class to manage the ship."""
    """Initialize the ship and set its starting position."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Get the directory path of the current script file.
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to the ship image.
        image_path = os.path.join(current_dir, 'images', 'ship3.bmp')
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)