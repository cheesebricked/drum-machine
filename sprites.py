import pygame
import settings

pygame.mixer.init()

box_width = (settings.SCREEN_WIDTH / settings.BEAT_LENGTH)
indicator_pos = 0

class BOX():
    def __init__(self, x, y, screen):
        self.rect = pygame.Rect(x, y, box_width, 50) #x, y, width, height
        self.surface = screen
        self.active = False
        self.color = (0, 0, 0)
        self.rect.topleft = (x, y)
        self.kick = pygame.mixer.Sound("kit/kick.wav")
        self.can_play = True

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)
        pygame.draw.rect(self.surface, (200, 200, 200), self.rect, 5)

    def check_click(self):
        self.m_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(self.m_pos): # is rect.collide_with(mouse), and is mouse clicked
            self.active = not self.active

    def change_color(self):
        if self.active:
            self.color = (0, 200, 0)
        else:
            self.color = (0, 0, 0)

    def check_indicator(self):
        self.m_pos = pygame.mouse.get_pos()
        global indicator_pos
        if indicator_pos == self.rect.x and self.active and self.can_play:
            pygame.mixer.Sound.play(self.kick)
            self.can_play = False
        if indicator_pos != self.rect.x:
            self.can_play = True

    def run(self):
        self.check_indicator()
        self.change_color()
        self.draw()  



class Indicator():
    def __init__(self, x, y, screen):
        self.indicator = pygame.Rect(x, y, box_width, settings.SCREEN_HEIGHT)
        self.surface = screen
        self.count = 0

    def draw(self):
        pygame.draw.rect(self.surface, (200,200,200), self.indicator)

    def tick(self):
        if self.indicator.x <= (settings.SCREEN_WIDTH - box_width):
            self.count += 1
            self.indicator.x = (settings.SCREEN_WIDTH * (self.count / (settings.BEAT_LENGTH)))
            global indicator_pos
            indicator_pos = self.indicator.x

        else:
            self.indicator.x = 0
            self.count = 0

    def run(self):
        self.draw()
