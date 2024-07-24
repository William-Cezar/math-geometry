import pygame
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.moving = False

    def draw(self, screen):
        center_x, center_y = screen.get_size()
        center_x //= 2
        center_y //= 2
        pygame.draw.circle(screen, (0, 0, 0), (center_x + self.x, center_y - self.y), self.radius, 2)

    def handle_event(self, event):
        center_x, center_y = screen.get_size()
        center_x //= 2
        center_y //= 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            distance = ((center_x + self.x - event.pos[0]) ** 2 + (center_y - self.y - event.pos[1]) ** 2) ** 0.5
            if distance <= self.radius:
                self.moving = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.moving = False
        elif event.type == pygame.MOUSEMOTION and self.moving:
            self.x += event.rel[0]
            self.y -= event.rel[1]
