import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Whack-a-Mole Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up game variables
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

class Circle:
    def __init__(self, filled, x):
        self.radius = 50
        self.x = x
        self.y = height // 2
        self.filled = filled

    def draw(self):
        color = RED if self.filled else BLACK
        pygame.draw.circle(display, color, (self.x, self.y), self.radius, 3 if not self.filled else 0)

# Create the circles
circles = [Circle(False, (i + 1) * (width // 6)) for i in range(4)]
circles.append(Circle(True, random.choice([(i + 1) * (width // 6) for i in range(5)])))

start_time = None
round_time = 1000  # 1 second in milliseconds

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_time is not None:
                elapsed_time = pygame.time.get_ticks() - start_time
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_circle = None
                for circle in circles:
                    distance = ((mouse_x - circle.x) ** 2 + (mouse_y - circle.y) ** 2) ** 0.5
                    if distance <= circle.radius and circle.filled:
                        clicked_circle = circle
                        break
                if clicked_circle is not None and elapsed_time <= round_time:
                    score += 1
                else:
                    score -= 1
                circles = [Circle(False, (i + 1) * (width // 6)) for i in range(4)]
                circles.append(Circle(True, random.choice([(i + 1) * (width // 6) for i in range(5)])))
                start_time = None

    display.fill(BLACK)

    for circle in circles:
        circle.draw()

    score_text = font.render(f"Score: {score}", True, WHITE)
    display.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

    if start_time is None and circles[-1].filled:
        start_time = pygame.time.get_ticks()
