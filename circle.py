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
        self.area_text = f'{radius * radius}\u03C0'

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
        self.draw_area_input(screen)
        self.draw_more_info_button(screen)

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
        circumference_text = font.render(f'Circumference: {self.circumference_text}', True, (0, 0, 0))
        screen.blit(circumference_text, (screen.get_width() - 250, 115))

    def draw_area_input(self, screen):
        font = pygame.font.Font(None, 36)
        input_box = pygame.Rect(screen.get_width() - 260, 160, 260, 40)
        pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
        area_text = font.render(f'Area: {self.area_text}', True, (0, 0, 0))
        screen.blit(area_text, (screen.get_width() - 250, 165))

    def draw_more_info_button(self, screen):
        font = pygame.font.Font(None, 36)
        button_rect = pygame.Rect(screen.get_width() - 260, 210, 260, 40)
        pygame.draw.rect(screen, (0, 0, 255), button_rect, 2)
        button_text = font.render('More Information', True, (0, 0, 255))
        screen.blit(button_text, (screen.get_width() - 250, 215))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(screen.get_width() - 260, 10, 260, 40).collidepoint(event.pos):
                self.active_input = 'radius'
            elif pygame.Rect(screen.get_width() - 260, 60, 260, 40).collidepoint(event.pos):
                self.active_input = 'diameter'
            elif pygame.Rect(screen.get_width() - 260, 210, 260, 40).collidepoint(event.pos):
                self.show_more_info()
            else:
                self.active_input = None
        elif event.type == pygame.KEYDOWN and self.active_input:
            if self.active_input == 'radius':
                if event.key == pygame.K_RETURN:
                    try:
                        self.radius = int(self.radius_text)
                        self.diameter_text = str(self.radius * 2)
                        self.circumference_text = f'{2 * self.radius}\u03C0' 
                        self.area_text = f'{self.radius * self.radius}\u03C0'
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
                        self.area_text = f'{self.radius * self.radius}\u03C0'
                    except ValueError:
                        self.diameter_text = str(self.radius * 2)
                    self.active_input = None
                elif event.key == pygame.K_BACKSPACE:
                    self.diameter_text = self.diameter_text[:-1]
                else:
                    self.diameter_text += event.unicode

    def show_more_info(self):
        # Create a new window and display more information
        more_info_screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("More Information")
        font = pygame.font.Font(None, 36)
        small_font = pygame.font.Font(None, 28)
        running = True
        while running:
            more_info_screen.fill((255, 255, 255))
            info_text = font.render("Information about Circle:", True, (0, 0, 0))
            more_info_screen.blit(info_text, (10, 10))

            explanations = [
                "A circle is a simple closed shape.",
                "It is the set of all points in a plane that are at a given distance",
                "from a given point, the centre.",
                "The distance between any of the points and the centre is called the radius.",
                "",
                "Equations:",
                "Radius (r): The distance from the center to the edge.",
                "Diameter (d): The distance across the circle, through the center. d = 2r.",
                "Circumference (C): The distance around the circle. C = 2πr.",
                "Area (A): The space enclosed by the circle. A = πr².",
                "The standard form equation of a circle with center (h,k) and radius r is:",
                "(x - h)² + (y - k)² = r²",
                "In our example",
                f"(x)² + (y)² = {self.radius}²",
            ]

            y_offset = 60
            for line in explanations:
                explanation_text = small_font.render(line, True, (0, 0, 0))
                more_info_screen.blit(explanation_text, (10, y_offset))
                y_offset += 40

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()

        pygame.display.set_mode((width, height))
        pygame.display.set_caption("Main Window")