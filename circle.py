import pygame
import math

width, height = 1200, 800
screen = pygame.display.set_mode((width, height))

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.active_input = None
        self.radius_text = str(radius)
        self.diameter_text = str(radius * 2)
        self.circumference_text = f'{2 * radius}\u03C0'

    def draw(self, screen):
        center_x, center_y = screen.get_size()
        center_x //= 2
        center_y //= 2
        
        # Draw the circle
        pygame.draw.circle(screen, (0, 0, 0), (center_x + self.x, center_y - self.y), self.radius, 2)
        
        # Calculate the end point of the radius line at a 45-degree angle
        angle = math.pi / 4  # 45 degrees in radians
        end_x = center_x + self.x + int(self.radius * math.cos(angle))
        end_y = center_y - self.y - int(self.radius * math.sin(angle))
        
        # Draw the radius line from the center to the calculated point
        pygame.draw.line(screen, (0, 0, 0), (center_x + self.x, center_y - self.y), (end_x, end_y), 2)
        
        # Label the radius line with "r"
        font = pygame.font.Font(None, 36)
        text = font.render('r', True, (0, 0, 0))
        text_rect = text.get_rect(center=(end_x - 20, end_y - 20))
        screen.blit(text, text_rect)
        
        # Draw the radius input box
        self.draw_radius_input(screen)
        self.draw_diameter_input(screen)
        self.draw_circumference_input(screen)

    def draw_radius_input(self, screen):
        font = pygame.font.Font(None, 36)
        input_box = pygame.Rect(screen.get_width() - 260, 10, 260, 40)
        if self.active_input == 'radius':
            pygame.draw.rect(screen, (0, 255, 0), input_box, 2)  # Green border when active
        else:
            pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
        radius_text = font.render(f'Radius: {self.radius_text}', True, (0, 0, 0))
        screen.blit(radius_text, (screen.get_width() - 250, 15))

    def draw_diameter_input(self, screen):
        font = pygame.font.Font(None, 36)
        input_box = pygame.Rect(screen.get_width() - 260, 60, 260, 40)
        if self.active_input == 'diameter':
            pygame.draw.rect(screen, (0, 255, 0), input_box, 2)
        else:
            pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
        diameter_text = font.render(f'Diameter: {self.diameter_text}', True, (0, 0, 0))
        screen.blit(diameter_text, (screen.get_width() - 250, 65))

    def draw_circumference_input(self, screen):
        font = pygame.font.Font(None, 36)
        input_box = pygame.Rect(screen.get_width() - 260, 110, 260, 40)
        pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
        circumference_text = font.render(f'Circunference: {self.circumference_text}', True, (0, 0, 0))
        screen.blit(circumference_text, (screen.get_width() - 250, 115))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(screen.get_width() - 210, 10, 200, 40).collidepoint(event.pos):
                self.active_input = 'radius'
            elif pygame.Rect(screen.get_width() - 210, 60, 200, 40).collidepoint(event.pos):
                self.active_input = 'diameter'
            else:
                self.active_input = None
        elif event.type == pygame.KEYDOWN and self.active_input:
            if self.active_input == 'radius':
                if event.key == pygame.K_RETURN:
                    try:
                        self.radius = int(self.radius_text)
                        self.diameter_text = str(self.radius * 2)
                        self.circumference_text = f'{2 * self.radius}\u03C0' 
                    except ValueError:
                        self.radius_text = str(self.radius)
                    self.active_input = None
                elif event.key == pygame.K_BACKSPACE:
                    self.radius_text = self.radius_text[:-1]
                else:
                    self.radius_text += event.unicode
            elif self.active_input == 'diameter':
                if event.key == pygame.K_RETURN:
                    try:
                        self.radius = int(int(self.diameter_text) / 2)
                        self.radius_text = str(self.radius)
                        self.circumference_text = f'{2 * self.radius}\u03C0' 
                    except ValueError:
                        self.diameter_text = str(self.radius * 2)
                    self.active_input = None
                elif event.key == pygame.K_BACKSPACE:
                    self.diameter_text = self.diameter_text[:-1]
                else:
                    self.diameter_text += event.unicode