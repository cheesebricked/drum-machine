import pygame


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BEAT_LENGTH = 32
BPM = 120
TICK_BEAT = (int(60000 / BPM))
TICK_8TH = (int((60000 / (BPM * 2))))
TICK_16TH = (int((60000 / (BPM * 4))))