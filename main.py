import pygame
import sprites
import settings
import render
from saves import saves

pygame.init()

run = True
play = False
clicked = False
scene = settings.SCREEN
clock = pygame.time.Clock()

box_list = render.box_list
num_list = render.num_list
indicator = sprites.Indicator((settings.LABEL_LENGTH), 0, scene)
menu = sprites.Menu(scene)

render.render()

ADVANCE = pygame.USEREVENT + 1
BPM_TICK = pygame.time.set_timer(ADVANCE, sprites.TICK_BEAT)
BPM_TICK

while run:
    scene.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # left click
            for b in box_list:
                b.check_click()
            for s in render.save_box_list:
                s.save()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            for s in render.save_box_list:
                s.load()
            BPM_TICK = pygame.time.set_timer(ADVANCE, sprites.TICK_BEAT)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # pause and play
            play = not play
        if event.type == ADVANCE and play: # moves indicator
            indicator.tick()
        if event.type == pygame.MOUSEWHEEL: # change bpm
            if menu.get_bpm() <= 1 and (event.__getattribute__('precise_y') < 0):
                menu.change_bpm(0)
            else:
                menu.change_bpm(int(event.__getattribute__('precise_y')))
            BPM_TICK = pygame.time.set_timer(ADVANCE, sprites.TICK_BEAT)





    indicator.run()     
    for b in box_list:
        b.run()
        if play:
            b.check_indicator()
    for n in num_list:
        n.draw()
    
    menu.run()

    for s in render.save_box_list:
        s.run()

    pygame.display.update()

    clock.tick(60)

pygame.quit()