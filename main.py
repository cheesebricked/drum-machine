import pygame
import sprites
import settings
import render

pygame.init()


run = True
clicked = False
scene = settings.SCREEN
clock = pygame.time.Clock()

box_list = render.box_list
indicator = sprites.Indicator(0, 0, scene)

ADVANCE = pygame.USEREVENT + 1
BPM_TICK = pygame.time.set_timer(ADVANCE, settings.TICK_8TH)
BPM_TICK

while run:
    scene.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for b in box_list:
                b.check_click()
        if event.type == ADVANCE:
            indicator.tick()

    indicator.run()     
    for b in box_list:
        b.run()

    pygame.display.update()

    clock.tick(60)

# FIX FIRST NOTE NOT PLAYING

pygame.quit()