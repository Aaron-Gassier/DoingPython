import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong")

# Set up colors
WHITE = (255, 255, 255)

# Set up paddles
paddle_width = 10
paddle_height = 60
paddle_speed = 5
left_paddle_x = 50
left_paddle_y = window_height // 2 - paddle_height // 2
right_paddle_x = window_width - 50 - paddle_width
right_paddle_y = window_height // 2 - paddle_height // 2

# Set up ball
ball_size = 10
ball_speed_x = 3
ball_speed_y = 3
ball_x = window_width // 2 - ball_size // 2
ball_y = window_height // 2 - ball_size // 2

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < window_height - paddle_height:
        left_paddle_y += paddle_speed
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < window_height - paddle_height:
        right_paddle_y += paddle_speed
    
    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Collision detection
    if ball_y <= 0 or ball_y >= window_height - ball_size:
        ball_speed_y *= -1
    if ball_x <= left_paddle_x + paddle_width and left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
        ball_speed_x *= -1
    if ball_x >= right_paddle_x - ball_size and right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
        ball_speed_x *= -1
    
    # Clear the screen
    window.fill(WHITE)
    
    # Draw paddles and ball
    pygame.draw.rect(window, WHITE, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(window, WHITE, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(window, WHITE, (ball_x, ball_y, ball_size, ball_size))
    
    # Update the display
    pygame.display.flip()
    
    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
