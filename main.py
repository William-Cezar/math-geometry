import pygame
import sys
from ellipse import Ellipse
from circle import Circle

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

# Center of the screen
center_x, center_y = width // 2, height // 2

# Objects
objects = {
    'Ellipse': Ellipse(0, 0, 500, 250),
    'Circle': Circle(0, 0, 300)
}
current_object_name = 'Ellipse'
current_object = objects[current_object_name]

# Dropdown properties
font = pygame.font.Font(None, 36)
dropdown_open = False

def draw_axes():
    pygame.draw.line(screen, gray, (center_x, 0), (center_x, height), 1)  # Y-axis
    pygame.draw.line(screen, gray, (0, center_y), (width, center_y), 1)  # X-axis

def to_cartesian(x, y):
    return center_x + x, center_y - y

def draw_dropdown():
    global dropdown_open
    dropdown_rect = pygame.Rect(10, 10, 200, 40)
    pygame.draw.rect(screen, black, dropdown_rect, 2)
    screen.blit(font.render(current_object_name, True, black), (20, 15))

    if dropdown_open:
        options_rect = pygame.Rect(10, 50, 200, 100)
        pygame.draw.rect(screen, black, options_rect, 2)
        for idx, obj_name in enumerate(objects.keys()):
            option_rect = pygame.Rect(10, 50 + idx * 40, 200, 40)
            pygame.draw.rect(screen, black, option_rect, 2)
            screen.blit(font.render(obj_name, True, black), (20, 55 + idx * 40))

def main():
    global current_object_name, current_object, dropdown_open

    while True:
        screen.fill(white)
        draw_axes()
        draw_dropdown()
        current_object.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if dropdown_open:
                    for idx, obj_name in enumerate(objects.keys()):
                        if pygame.Rect(10, 50 + idx * 40, 200, 40).collidepoint(event.pos):
                            current_object_name = obj_name
                            current_object = objects[obj_name]
                            dropdown_open = False
                            break
                else:
                    if pygame.Rect(10, 10, 200, 40).collidepoint(event.pos):
                        dropdown_open = True
                current_object.handle_event(event)
            else:
                current_object.handle_event(event)

        pygame.display.flip()

if __name__ == "__main__":
    main()
