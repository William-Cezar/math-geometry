import pygame
import math

# Screen dimensions
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))

class Ellipse:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.active_input = None
        self.a_text = str(width / 2)
        self.b_text = str(height / 2)
        self.area_text = f'{math.pi * (width / 2) * (height / 2):.2f}'
        self.c_text = f'{math.sqrt((width / 2)**2 - (height / 2)**2):.2f}'
        self.circumference_text = f'{math.pi * (3*(width / 2 + height / 2) - math.sqrt((3 * width / 2 + height / 2) * (width / 2 + 3 * height / 2))):.2f}'

    def draw(self, screen):
        center_x, center_y = screen.get_size()
        center_x //= 2
        center_y //= 2
        rect = pygame.Rect(center_x + self.x - self.width // 2, center_y - self.y - self.height // 2, self.width, self.height)
        pygame.draw.ellipse(screen, (0, 0, 0), rect, 2)

        self.draw_axes(screen, center_x, center_y)
        self.draw_focal_points(screen, center_x, center_y)
        self.draw_focal_length(screen, center_x, center_y)
        self.draw_a_input(screen)
        self.draw_b_input(screen)
        self.draw_c_input(screen)
        self.draw_circumference_input(screen)
        self.draw_area_input(screen)
        self.draw_more_info_button(screen)

    def draw_axes(self, screen, center_x, center_y):
        # Semi-major axis
        pygame.draw.line(screen, (0, 0, 255), (center_x - self.width // 2, center_y), (center_x + self.width // 2, center_y), 2)
        font = pygame.font.Font(None, 36)
        text = font.render('A=2a', True, (0, 0, 255))
        screen.blit(text, (center_x + self.width // 2 + 10, center_y - 20))

        # Semi-minor axis
        pygame.draw.line(screen, (0, 0, 255), (center_x, center_y - self.height // 2), (center_x, center_y + self.height // 2), 2)
        text = font.render('B=2b', True, (0, 0, 255))
        screen.blit(text, (center_x + 10, center_y - self.height // 2 - 20))

    def draw_focal_points(self, screen, center_x, center_y):
        a = self.width / 2
        b = self.height / 2
        c = math.sqrt(a**2 - b**2)
        focal_points = [(center_x - c, center_y), (center_x + c, center_y)]

        for fp in focal_points:
            pygame.draw.circle(screen, (255, 0, 0), fp, 5)
            pygame.draw.line(screen, (255, 0, 0), fp, (center_x, center_y + b), 2)
        font = pygame.font.Font(None, 36)
        text = font.render('F', True, (255, 0, 0))
        screen.blit(text, (center_x - c + 10, center_y - 20))
        screen.blit(text, (center_x + c + 10, center_y - 20))
        
        # Label the distance from focal points to semi-minor axis intersection
        text = font.render('a', True, (255, 0, 0))
        screen.blit(text, (center_x - c / 2, center_y + b // 2))
        screen.blit(text, (center_x + c / 2, center_y + b // 2))

    def draw_focal_length(self, screen, center_x, center_y):
        a = self.width / 2
        b = self.height / 2
        c = math.sqrt(a**2 - b**2)
        focal_point = (center_x - c, center_y)
        pygame.draw.line(screen, (0, 255, 0), (center_x, center_y), focal_point, 2)
        font = pygame.font.Font(None, 36)
        text = font.render('c', True, (0, 255, 0))
        text_rect = text.get_rect(center=((center_x + focal_point[0]) // 2, center_y - 20))
        screen.blit(text, text_rect)

    def draw_a_input(self, screen):
        font = pygame.font.Font(None, 36)
        input_box = pygame.Rect(screen.get_width() - 330, 10, 320, 40)
        if self.active_input == 'a':
            pygame.draw.rect(screen, (0, 255, 0), input_box, 2)  # Green border when active
        else:
            pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
        a_text = font.render(f'Semi-major axis (a): {self.a_text}', True, (0, 0, 0))
        screen.blit(a_text, (screen.get_width() - 325, 15))

    def draw_b_input(self, screen):
        font = pygame.font.Font(None, 36)
        input_box = pygame.Rect(screen.get_width() - 330, 60, 320, 40)
        if self.active_input == 'b':
            pygame.draw.rect(screen, (0, 255, 0), input_box, 2)
        else:
            pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
        b_text = font.render(f'Semi-minor axis (b): {self.b_text}', True, (0, 0, 0))
        screen.blit(b_text, (screen.get_width() - 325, 65))

    def draw_c_input(self, screen):
        font = pygame.font.Font(None, 36)
        input_box = pygame.Rect(screen.get_width() - 330, 110, 320, 40)
        pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
        c_text = font.render(f'Focal length (c): {self.c_text}', True, (0, 0, 0))
        screen.blit(c_text, (screen.get_width() - 325, 115))

    def draw_circumference_input(self, screen):
        font = pygame.font.Font(None, 36)
        input_box = pygame.Rect(screen.get_width() - 330, 160, 320, 40)
        pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
        circumference_text = font.render(f'Circumference: {self.circumference_text}', True, (0, 0, 0))
        screen.blit(circumference_text, (screen.get_width() - 325, 165))

    def draw_area_input(self, screen):
        font = pygame.font.Font(None, 36)
        input_box = pygame.Rect(screen.get_width() - 330, 210, 320, 40)
        pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
        area_text = font.render(f'Area: {self.area_text}', True, (0, 0, 0))
        screen.blit(area_text, (screen.get_width() - 325, 215))

    def draw_more_info_button(self, screen):
        font = pygame.font.Font(None, 36)
        button_rect = pygame.Rect(screen.get_width() - 330, 260, 320, 40)
        pygame.draw.rect(screen, (0, 0, 255), button_rect, 2)
        button_text = font.render('More Information', True, (0, 0, 255))
        screen.blit(button_text, (screen.get_width() - 325, 265))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(screen.get_width() - 260, 10, 260, 40).collidepoint(event.pos):
                self.active_input = 'a'
            elif pygame.Rect(screen.get_width() - 260, 60, 260, 40).collidepoint(event.pos):
                self.active_input = 'b'
            elif pygame.Rect(screen.get_width() - 260, 260, 260, 40).collidepoint(event.pos):
                self.show_more_info()
            else:
                self.active_input = None
        elif event.type == pygame.KEYDOWN and self.active_input:
            if self.active_input == 'a':
                if event.key == pygame.K_RETURN:
                    try:
                        self.width = float(self.a_text) * 2
                        self.area_text = f'{math.pi * (self.width / 2) * (self.height / 2):.2f}'
                        self.c_text = f'{math.sqrt((self.width / 2)**2 - (self.height / 2)**2):.2f}'
                        self.circumference_text = f'{math.pi * (3*(self.width / 2 + self.height / 2) - math.sqrt((3 * self.width / 2 + self.height / 2) * (self.width / 2 + 3 * self.height / 2))):.2f}'
                    except ValueError:
                        self.a_text = str(self.width / 2)
                    self.active_input = None
                elif event.key == pygame.K_BACKSPACE:
                    self.a_text = self.a_text[:-1]
                else:
                    self.a_text += event.unicode
            elif self.active_input == 'b':
                if event.key == pygame.K_RETURN:
                    try:
                        self.height = float(self.b_text) * 2
                        self.area_text = f'{math.pi * (self.width / 2) * (self.height / 2):.2f}'
                        self.c_text = f'{math.sqrt((self.width / 2)**2 - (self.height / 2)**2):.2f}'
                        self.circumference_text = f'{math.pi * (3*(self.width / 2 + self.height / 2) - math.sqrt((3 * self.width / 2 + self.height / 2) * (self.width / 2 + 3 * self.height / 2))):.2f}'
                    except ValueError:
                        self.b_text = str(self.height / 2)
                    self.active_input = None
                elif event.key == pygame.K_BACKSPACE:
                    self.b_text = self.b_text[:-1]
                else:
                    self.b_text += event.unicode

    def show_more_info(self):
        # Create a new window and display more information
        more_info_screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("More Information")
        font = pygame.font.Font(None, 36)
        small_font = pygame.font.Font(None, 28)
        running = True
        while running:
            more_info_screen.fill((255, 255, 255))
            info_text = font.render("Information about Ellipse:", True, (0, 0, 0))
            more_info_screen.blit(info_text, (10, 10))

            explanations = [
                "An ellipse is a curve on a plane surrounding two focal points.",
                "The sum of the distances to the two focal points is constant.",
                "The longest diameter of the ellipse is called the major axis.",
                "The shortest diameter of the ellipse is called the minor axis.",
                "",
                "Equations:",
                "Semi-major axis (a): Half of the longest diameter.",
                "Semi-minor axis (b): Half of the shortest diameter.",
                "Circumference (C): An approximation is C = π [ 3(a + b) - √((3a + b)(a + 3b)) ].",
                "Area (A): A = πab.",
                "Focal length (c): c = √(a² - b²).",
                "",
                "Standard Form Equation:",
                f"(x - {self.x})² / a² + (y - {self.y})² / b² = 1",
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
