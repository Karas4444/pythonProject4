import pygame
from pon import *
from sprites import Player

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()

players_spriters = pygame.sprite.Group() # слздаю группу спрайтов
player = Player() # создаю спрайт героя
players_spriters.add(player) # добавляю группу

running = True
while running:
    # FPS контроль
    clock.tick(FPS)

    players_spriters.update()

    # рендеринг
    screen.fill(GREEN)
    players_spriters.draw(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



pygame.quit()