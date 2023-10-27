import pygame
import sprites
import settings
import render

pygame.init()


run = True
play = False
clicked = False
scene = settings.SCREEN
clock = pygame.time.Clock()

box_list = render.box_list
num_list = render.num_list
indicator = sprites.Indicator((settings.LABEL_LENGTH), 0, scene)

ADVANCE = pygame.USEREVENT + 1
BPM_TICK = pygame.time.set_timer(ADVANCE, settings.TICK_BEAT)
BPM_TICK

while run:
    scene.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for b in box_list:
                b.check_click()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            play = not play
        if event.type == ADVANCE and play:
            indicator.tick()


    indicator.run()     
    for b in box_list:
        b.run()
        if play:
            b.check_indicator()
    for n in num_list:
        n.draw()

    pygame.display.update()

    clock.tick(60)

pygame.quit()