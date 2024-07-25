import pygame
# Screen dimensions
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))

class Ellipse:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.moving = False

    def draw(self, screen):
        center_x, center_y = screen.get_size()
        center_x //= 2
        center_y //= 2
        rect = pygame.Rect(center_x + self.x - self.width // 2, center_y - self.y - self.height // 2, self.width, self.height)
        pygame.draw.ellipse(screen, (0, 0, 0), rect, 2)

    def handle_event(self, event):
        pass
