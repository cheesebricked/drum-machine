import pygame
import sprites
import settings

box_list = []

def x_pos(n):
    return (settings.SCREEN_WIDTH * (n / (settings.BEAT_LENGTH)))

def position_boxes(scene):
    for i in range(settings.BEAT_LENGTH):
        box_list.append(sprites.BOX(round(x_pos(i), 0), 200, scene))

position_boxes(settings.SCREEN)

