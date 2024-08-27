import pygame
import sys
import random

# 초기화
pygame.init()

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("블록 깨기 게임")

# 프레임 속도 설정
clock = pygame.time.Clock()

# 패들 클래스 정의
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([100, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - 50
        self.rect.y = SCREEN_HEIGHT - 20
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - 100:
            self.rect.x = SCREEN_WIDTH - 100

# 공 클래스 정의
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - 5
        self.rect.y = SCREEN_HEIGHT // 2 - 5
        self.speed_x = random.choice([-5, 5])
        self.speed_y = -5

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # 벽에 부딪히면 튕기기
        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - 10:
            self.speed_x = -self.speed_x
        if self.rect.y <= 0:
            self.speed_y = -self.speed_y
        if self.rect.y >= SCREEN_HEIGHT:
            self.speed_y = -5
            self.rect.x = SCREEN_WIDTH // 2 - 5
            self.rect.y = SCREEN_HEIGHT // 2 - 5

# 블록 클래스 정의
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([50, 20])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# 스프라이트 그룹 설정
all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()

paddle = Paddle()
all_sprites.add(paddle)

ball = Ball()
all_sprites.add(ball)

# 블록 생성
for i in range(7):
    for j in range(5):
        block = Block(60 + i * 60, 40 + j * 30)
        all_sprites.add(block)
        blocks.add(block)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.speed_x = -6
            elif event.key == pygame.K_RIGHT:
                paddle.speed_x = 6
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle.speed_x = 0

    all_sprites.update()

    # 공이 패들에 닿으면 튕기기
    if pygame.sprite.collide_rect(ball, paddle):
        ball.speed_y = -ball.speed_y

    # 공이 블록에 닿으면 튕기고 블록 제거
    block_hit_list = pygame.sprite.spritecollide(ball, blocks, True)
    if block_hit_list:
        ball.speed_y = -ball.speed_y
        for block in block_hit_list:
            blocks.remove(block)

    # 모든 블록이 깨지면 게임 종료
    if not blocks:
        running = False

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
