import pygame
import sprites
import settings

box_list = []
num_list = []

def x_pos(n):
    return (((settings.SCREEN_WIDTH - settings.LABEL_LENGTH) * (n / (settings.BEAT_LENGTH))) + settings.LABEL_LENGTH)

def position_boxes(scene):
    for s in settings.SOUND_LIST:
        for i in range(settings.BEAT_LENGTH):
            box_list.append(sprites.BOX(x_pos(i), (((settings.SOUND_LIST.index(s)) * settings.BOX_HEIGHT) + settings.BEAT_NUMBER_HEIGHT), scene, s))

def position_numbers(scene):
    for i in range(settings.BEAT_LENGTH):
        num_list.append(sprites.BeatNumber((x_pos(i) + (sprites.box_width / 3)), 0, str(i + 1), scene))

position_boxes(settings.SCREEN)
position_numbers(settings.SCREEN)

