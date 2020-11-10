import pygame
import sys

W, H = 800, 600
collide = False
collide2 = False
block = False
block2 = False
n = 0
m = 0
# Квадрат
rect_size = w, h = 70, 70
rect_pos = ((W - w) // 2, (H - h) // 2)
# Круг
circle_radius = 35
circle_pos = (0, 0)
# Цвета
RED = (250, 0, 0, 180)
BLUE = (0, 0, 250, 180)
YELLOW = (250, 250, 0, 180)
BG = (128, 128, 128)

speed = [5, 5]

pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
screen = pygame.display.set_mode((W, H))
font = pygame.font.Font(None, 32)
# создаем поверхность размером в 2-а раза больше радиуса круга и вкл. альфа-канал
surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
# на созданной поверхности рисуем круг желтого цвета
pygame.draw.circle(surface, YELLOW, (circle_radius, circle_radius), circle_radius)
# находим рект у поверхности
rect1 = surface.get_rect()

clock = pygame.time.Clock()
FPS = 120

ball_image = pygame.image.load('ball.png')
ball_rect = ball_image.get_rect(topleft=(0, 0))


def abc(x,y):
    if ball_rect.left < 0 or ball_rect.right > W:
        speed[0] = -x
    elif ball_rect.top < 0 or ball_rect.bottom > H:
        speed[1] = -y
    return ball_rect.move(speed)


while True:
    clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
        elif e.type == pygame.MOUSEMOTION:
            # circle_pos = e.pos
            rect1.center = e.pos

    screen.fill(BG)
    COLOR = RED if collide else BLUE
    # rect1 = pygame.draw.circle(screen, YELLOW, circle_pos, circle_radius)
    rect2 = pygame.draw.rect(screen, COLOR, (rect_pos, rect_size))
    screen.blit(surface, rect1)

    if rect1.colliderect(rect2):
        if not collide:
            n += 1
            collide = True
    else:
        collide = False
    if ball_rect.colliderect(rect2):
        if not collide:
            m += 1
            collide2 = True
    else:
        collide2 = False

    ball_rect = abc(speed[0], speed[1])

    screen.blit(ball_image, ball_rect)
    screen.blit(font.render(str(n), 1, RED), (10, 10))
    screen.blit(font.render(str(n), 1, RED), (W - 30, 10))
    pygame.display.update()
