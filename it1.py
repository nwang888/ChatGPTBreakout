import pygame

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

paddle_x, paddle_y = (width // 2) - (paddle_width // 2), height - paddle_height
ball_x, ball_y = width // 2, height // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT]:
        paddle_x += paddle_speed

    ball_x += ball_x_speed
    ball_y += ball_y_speed

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_radius)
    pygame.display.update()
