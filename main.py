import pygame
from constants import *
from visuals import *

pygame.init()

infoObject = pygame.display.Info()

screen_w = int(infoObject.current_w/2.5)
screen_h = int(infoObject.current_w/2.5)

screen = pygame.display.set_mode([screen_w, screen_h])

# audio bars
bars = setup_bars(screen_w)

t = pygame.time.get_ticks()
getTicksLastFrame = t

pygame.mixer.music.load(filename)
pygame.mixer.music.play(0)

running = True
while running:

    t = pygame.time.get_ticks()
    delta_time = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    update_bars(bars, screen, delta_time, pygame.mixer.music.get_pos())

    pygame.display.flip()

pygame.quit()
