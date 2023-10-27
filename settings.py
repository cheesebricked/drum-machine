import pygame


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BEAT_LENGTH = 16
BPM = 120
SUBDIVISION = 16

TICK_BEAT = (int(60000 / (BPM * (SUBDIVISION / 4))))

BEAT_NUMBER_HEIGHT = 20

LABEL_LENGTH = 200

SOUND_LIST = ["kick", "snare", "hat_c", "hat_o", "tom1", "tom2", "cowbell"]

MENU_HEIGHT = 300

BOX_HEIGHT = ((SCREEN_HEIGHT / len(SOUND_LIST)) - (MENU_HEIGHT / len(SOUND_LIST)))

