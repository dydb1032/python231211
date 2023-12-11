import pygame
import random

# 게임 초기화
pygame.init()

# 화면 크기 설정
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("블록 깨기")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# 패들 설정
paddle_width = 100
paddle_height = 10
paddle_x = screen_width // 2 - paddle_width // 2
paddle_y = screen_height - 30
paddle_speed = 3  # 패들의 속도를 낮춤

# 공 설정
ball_radius = 10
ball_x = random.randint(ball_radius, screen_width - ball_radius)
ball_y = screen_height // 2
ball_dx = 3
ball_dy = 3

# 블록 설정
block_width = 50
block_height = 20
blocks = []
block_rows = 5
block_cols = screen_width // block_width

for row in range(block_rows):
    for col in range(block_cols):
        block = pygame.Rect(col * block_width, row * block_height, block_width, block_height)
        blocks.append(block)

# 게임 루프
running = True
clock = pygame.time.Clock()
fps = 30

while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
        ball_dx = -ball_dx
    if ball_y - ball_radius <= 0:
        ball_dy = -ball_dy

    if ball.colliderect(pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)) and ball_dy > 0:
        ball_dy = -ball_dy

    for block in blocks[:]:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_dy = -ball_dy

    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(screen, green, (paddle_x, paddle_y, paddle_width, paddle_height))

    for block in blocks:
        pygame.draw.rect(screen, blue, block)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
