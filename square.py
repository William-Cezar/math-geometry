import pygame
import math

# Screen dimensions
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))

class Square:
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def draw(self, screen):
        center_x, center_y = screen.get_size()
        center_x //= 2
        center_y //= 2

        # Define the top-left corner of the square
        top_left_x = center_x + self.x - self.side_length // 2
        top_left_y = center_y - self.y - self.side_length // 2

        # Draw the square
        pygame.draw.rect(screen, (0, 0, 0), (top_left_x, top_left_y, self.side_length, self.side_length), 2)
    
    def handle_event(self, event):
        pass