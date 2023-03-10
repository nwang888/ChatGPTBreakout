import pygame

# Initialize pygame
pygame.init()

# Initialize font
font = pygame.font.SysFont('Calibri', 35, bold=False, italic=False)

# Set the screen size
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the screen
pygame.display.set_caption("Atari Breakout")

# Set the initial positions of the paddle and the ball
paddle_width, paddle_height = 80, 15
paddle_x, paddle_y = (screen_width // 2) - (paddle_width // 2), screen_height - paddle_height
paddle_speed = 2

ball_x, ball_y = screen_width // 2, screen_height // 2
ball_radius = 8
ball_x_speed, ball_y_speed = 2, -2

class Brick:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hit = False

def create_bricks():
    bricks = []
    brick_x_offset = 75
    brick_y_offset = 50
    brick_width = 50
    brick_height = 20
    brick_spacing = 10
    for row in range(5):
        for col in range(10):
            brick_x = brick_x_offset + (brick_width + brick_spacing) * col
            brick_y = brick_y_offset + (brick_height + brick_spacing) * row
            brick = Brick(brick_x, brick_y, brick_width, brick_height)
            bricks.append(brick)
    return bricks


# Create a list of bricks
bricks = []
for i in range(5):
    for j in range(5):
        bricks.append(Brick(i * 100 + 30, j * 25 + 50, 80, 20))

# Function to check for collision between the ball and the paddle
def check_paddle_collision(ball_x, ball_y, paddle_x, paddle_y, paddle_width, paddle_height, ball_radius):
    if (ball_x + ball_radius >= paddle_x and ball_x - ball_radius <= paddle_x + paddle_width) and (ball_y + ball_radius >= paddle_y and ball_y - ball_radius <= paddle_y + paddle_height):
        return True
    return False

# Function to check for collision between the ball and the brick
def check_brick_collision(ball_x, ball_y, brick_x, brick_y, brick_width, brick_height):
    if (ball_x + ball_radius >= brick_x and ball_x - ball_radius <= brick_x + brick_width) and (ball_y + ball_radius >= brick_y and ball_y - ball_radius <= brick_y + brick_height):
        return True
    return False

ball_speed = 0.5
ball_x_speed = ball_speed
ball_y_speed = ball_speed

score = 0

# Initialize game variables
score = 0
ball_x, ball_y = screen_width/2, screen_height/2
ball_x_speed, ball_y_speed = ball_speed, ball_speed
paddle_x, paddle_y = (screen_width - paddle_width)/2, screen_height - paddle_height - 10
bricks = create_bricks()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT]:
        paddle_x += paddle_speed

    # Check for collision between the ball and the paddle
    if check_paddle_collision(ball_x, ball_y, paddle_x, paddle_y, paddle_width, paddle_height, ball_radius):
        # Reverse the ball's y-velocity
        ball_y_speed = -ball_speed
        # Change the x-velocity of the ball depending on where it hit the paddle
        ball_x_speed = (ball_x - (paddle_x + paddle_width / 2)) * 0.1
    # Check for collision between the ball and the bricks
    for brick in bricks:
        if ball_x + ball_radius > brick.x and ball_x - ball_radius < brick.x + brick.width:
            if ball_y + ball_radius > brick.y and ball_y - ball_radius < brick.y + brick.height:
                ball_y_speed = -ball_y_speed
                if ball_x_speed > 0:  # moving from left to right
                    if ball_x + ball_radius > brick.x and ball_x + ball_radius < brick.x + brick.width / 2 and (
                            ball_y + ball_radius > brick.y or ball_y - ball_radius < brick.y + brick.height):
                        ball_x_speed = -ball_x_speed
                else:  # moving from right to left
                    if ball_x - ball_radius < brick.x + brick.width and ball_x - ball_radius > brick.x + brick.width / 2 and (
                            ball_y + ball_radius > brick.y or ball_y - ball_radius < brick.y + brick.height):
                        ball_x_speed = -ball_x_speed
                bricks.remove(brick)
                score += 1
                break
    # Check for collision between the ball and the left edge of the screen
    if ball_x - ball_radius <= 0:
        ball_x_speed = abs(ball_x_speed)
    # Check for collision between the ball and the right edge of the screen
    elif ball_x + ball_radius >= screen_width:
        ball_x_speed = -abs(ball_x_speed)
    # Check for collision between the ball and the top edge of the screen
    if ball_y - ball_radius <= 0:
        ball_y_speed = abs(ball_y_speed)

    # Move the ball based on its x and y velocities
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    # Check for collision between the ball and the bottom edge of the screen
    if ball_y + ball_radius > screen_height:
        # Reinitialize game variables
        score = 0
        ball_x, ball_y = screen_width/2, screen_height/2
        ball_x_speed, ball_y_speed = ball_speed, ball_speed
        paddle_x, paddle_y = (screen_width - paddle_width)/2, screen_height - paddle_height - 10
        bricks = create_bricks()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the bricks
    for brick in bricks:
        pygame.draw.rect(screen, (255, 0, 0), (brick.x, brick.y, brick.width, brick.height))

    # Draw the paddle
    pygame.draw.rect(screen, (255, 255, 255), (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw the ball
    pygame.draw.circle(screen, (255, 255, 255), (int(ball_x), int(ball_y)), ball_radius)

    # Draw the score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.update()