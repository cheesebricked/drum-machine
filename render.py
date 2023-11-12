import pygame
import sprites
import settings

box_list = []
num_list = []
bar_start = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
save_box_list = []

save_box_size = 35

#for beat boxes
def outline_color(n):
    if n in bar_start:
        return (200, 200, 200)
    else:
        return (69, 69, 69)

def x_pos(n):
    return (((settings.SCREEN_WIDTH - settings.LABEL_LENGTH) * (n / (settings.BEAT_LENGTH))) + settings.LABEL_LENGTH)

def position_boxes(scene):
    for s in settings.SOUND_LIST:
        for i in range(settings.BEAT_LENGTH):
            box_list.append(sprites.BOX(x_pos(i), (((settings.SOUND_LIST.index(s)) * settings.BOX_HEIGHT) + settings.BEAT_NUMBER_HEIGHT), scene, s, outline_color(i)))

def position_numbers(scene):
    for i in range(settings.BEAT_LENGTH):
        num_list.append(sprites.BeatNumber((x_pos(i) + (sprites.box_width / 3)), 0, str(i + 1), scene))

#for saves
def position_saves():
    for s in range(4):
        save_box_list.append(sprites.Saves( (((settings.SCREEN_WIDTH / 10) * 7) + (s * (save_box_size * 1.1))), ((settings.SCREEN_HEIGHT - settings.MENU_HEIGHT) + ((settings.SCREEN_HEIGHT - settings.MENU_HEIGHT) / 20)), (s + 1), settings.SCREEN, save_box_size))
    for s in range(4):
        save_box_list.append(sprites.Saves( (((settings.SCREEN_WIDTH / 10) * 7) + (s * (save_box_size * 1.1))), (((settings.SCREEN_HEIGHT - settings.MENU_HEIGHT) + (save_box_size * 1.1)) + ((settings.SCREEN_HEIGHT - settings.MENU_HEIGHT) / 20)), (s + 5), settings.SCREEN, save_box_size))

def render():
    position_boxes(settings.SCREEN)
    position_numbers(settings.SCREEN)

    position_saves()



