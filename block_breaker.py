import pygame
import random

# 초기화
pygame.init()

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

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
        if self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width

    def expand(self):
        self.rect.width += 30
        self.image = pygame.Surface([self.rect.width, 10])
        self.image.fill(WHITE)

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

        # 바닥에 닿으면 패들 위로 리셋
        if self.rect.y >= SCREEN_HEIGHT:
            self.rect.x = SCREEN_WIDTH // 2 - 5
            self.rect.y = SCREEN_HEIGHT // 2 - 5
            self.speed_y = -5

# 블록 클래스 정의
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([50, 20])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# 아이템 클래스 정의
class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, effect):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.effect = effect

        if effect == "expand":
            self.image.fill(YELLOW)
        elif effect == "multi_ball":
            self.image.fill(BLUE)
        elif effect == "shoot":
            self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += 3
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()

# 총알 클래스 정의
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([5, 15])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= 5
        if self.rect.y < 0:
            self.kill()

# 스프라이트 그룹 설정
all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
blocks = pygame.sprite.Group()
items = pygame.sprite.Group()
bullets = pygame.sprite.Group()

paddle = Paddle()
all_sprites.add(paddle)

ball = Ball()
all_sprites.add(ball)
balls.add(ball)

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
            elif event.key == pygame.K_SPACE:
                bullet = Bullet(paddle.rect.centerx, paddle.rect.y)
                all_sprites.add(bullet)
                bullets.add(bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle.speed_x = 0

    # 게임 상태 업데이트
    all_sprites.update()

    # 공이 패들에 닿으면 튕기기
    for ball in balls:
        if pygame.sprite.collide_rect(ball, paddle):
            ball.speed_y = -ball.speed_y

    # 공이 블록에 닿으면 튕기고 블록 제거 및 아이템 생성
    for ball in balls:
        block_hit_list = pygame.sprite.spritecollide(ball, blocks, True)
        for block in block_hit_list:
            ball.speed_y = -ball.speed_y
            if random.random() < 0.3:  # 30% 확률로 아이템 생성
                effect = random.choice(["expand", "multi_ball", "shoot"])
                item = Item(block.rect.x, block.rect.y, effect)
                all_sprites.add(item)
                items.add(item)

    # 아이템이 패들에 닿으면 효과 발동
    item_hit_list = pygame.sprite.spritecollide(paddle, items, True)
    for item in item_hit_list:
        if item.effect == "expand":
            paddle.expand()
        elif item.effect == "multi_ball":
            for _ in range(2):  # 공 두 개 추가
                new_ball = Ball()
                new_ball.rect.x = paddle.rect.centerx
                new_ball.rect.y = paddle.rect.y - 10
                all_sprites.add(new_ball)
                balls.add(new_ball)
        elif item.effect == "shoot":
            bullet = Bullet(paddle.rect.centerx, paddle.rect.y)
            all_sprites.add(bullet)
            bullets.add(bullet)

    # 총알이 블록에 닿으면 블록 제거
    bullet_hit_list = pygame.sprite.groupcollide(bullets, blocks, True, True)

    # 모든 블록이 깨지면 게임 종료
    if not blocks:
        running = False

    # 화면 그리기
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    # 프레임 조절
    clock.tick(60)

pygame.quit()
