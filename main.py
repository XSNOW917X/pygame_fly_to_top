# print("hello game")
from platform import platform
from turtle import Screen
import pygame
import os

pygame.init()
pygame.display.set_caption("Fly To Top")


FPS = 60

# loding img
plane_img = pygame.image.load(os.path.join(
    "img", "TWplane.png"))
plane_mini_img = pygame.transform.scale(plane_img,(25,19))
pygame.display.set_icon(plane_mini_img)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
WIDTH = 1920
HIGTH = 1020

screen = pygame.display.set_mode((WIDTH, HIGTH))
clock = pygame.time.Clock()
running = True
MOVING_SPEED = 2

PLANE_WIDTH = 125
PLANE_HIGTH = 175

font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)


def draw_init():
    draw_text(screen, 'Photosensitive seizure warning', 64, WIDTH/2, HIGTH/4)
    draw_text(screen, 'Press any key to start', 24, WIDTH/2, HIGTH/2)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYUP:
                waiting = False
                return False


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # pygame.Surface((PLANE_WIDTH, PLANE_HIGTH))
        self.image = pygame.transform.scale(plane_img, (50, 70))
        self.image.set_colorkey(BLACK)
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2
        self.rect.y = HIGTH*0.8

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            self.rect.x += MOVING_SPEED
        if key_pressed[pygame.K_w]:
            self.rect.y -= MOVING_SPEED
        if key_pressed[pygame.K_a]:
            self.rect.x -= MOVING_SPEED
        if key_pressed[pygame.K_s]:
            self.rect.y += MOVING_SPEED
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += MOVING_SPEED
        if key_pressed[pygame.K_UP]:
            self.rect.y -= MOVING_SPEED
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= MOVING_SPEED
        if key_pressed[pygame.K_DOWN]:
            self.rect.y += MOVING_SPEED

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HIGTH:
            self.rect.bottom = HIGTH


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

countR = 1
countG = 1
countB = 1

show_init = True

running = True
while running:
    if show_init:
        close = draw_init()
        if close:
            break
        
        show_init = False

    # input
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or player.rect.top < 0:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.rect.y -= 50

    # update game
    all_sprites.update()

    # screen
    countR += 0.1
    countG += 0.3
    countB += 0.5
    screen.fill((countR % 255, countG % 255, countB % 255))
    all_sprites.draw(screen)
    pygame.display.update()


pygame.quit()
