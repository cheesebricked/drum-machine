import pygame
import settings

pygame.mixer.init()
pygame.font.init()

box_width = (settings.SCREEN_WIDTH / settings.BEAT_LENGTH)
indicator_pos = (settings.LABEL_LENGTH)
box_height = settings.BOX_HEIGHT
label_font = pygame.font.SysFont("Arial", 30)
label_font_small = pygame.font.SysFont("Arial", 15)

class BOX():
    def __init__(self, x, y, screen, sample):
        self.rect = pygame.Rect(x, y, box_width, box_height) #x, y, width, height
        self.label_rect = pygame.Rect(0, y, settings.LABEL_LENGTH, box_height)
        self.surface = screen
        self.active = False
        self.sound = sample
        self.color = (0, 0, 0)
        self.rect.topleft = (x, y)
        self.kick = pygame.mixer.Sound(f"kit/{self.sound}.wav")
        self.can_play = True
        self.x = x
        self.y = y

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
        global indicator_pos
        if indicator_pos == self.rect.x and self.active and self.can_play:
            pygame.mixer.Sound.play(self.kick)
            self.can_play = False
        if indicator_pos != self.rect.x:
            self.can_play = True

    def draw_label_text(self, text):
        self.label = label_font.render(text, True, (200,200,200))
        self.surface.blit(self.label, ((settings.LABEL_LENGTH / 10), (self.y + (box_height / 10))))

    def draw_label(self):
        pygame.draw.rect(self.surface, (0, 0, 0), self.label_rect)
        pygame.draw.rect(self.surface, (200,200,200), self.label_rect, 5)
        self.draw_label_text(self.sound)

    def run(self):
        self.draw_label()
        self.change_color()
        self.draw()

class BeatNumber():
    def __init__(self, x, y, text, scene):
        self.num_text = label_font_small.render(text, True, (200,200,200))
        self.x = x
        self.y = y
        self.surface = scene
    
    def draw(self):
        self.surface.blit(self.num_text, (self.x, self.y))

class Indicator():
    def __init__(self, x, y, screen):
        self.indicator = pygame.Rect(x, y, box_width, settings.SCREEN_HEIGHT)
        self.surface = screen
        self.count = 0

    def draw(self):
        pygame.draw.rect(self.surface, (200,200,200), self.indicator)

    def tick(self):
        if self.indicator.x < (settings.SCREEN_WIDTH - box_width):
            self.count += 1
            self.indicator.x = (((settings.SCREEN_WIDTH - + settings.LABEL_LENGTH) * (self.count / (settings.BEAT_LENGTH))) + settings.LABEL_LENGTH)
            global indicator_pos
            indicator_pos = self.indicator.x

        else:
            self.indicator.x = (settings.LABEL_LENGTH)
            indicator_pos = self.indicator.x
            self.count = 0

    def run(self):
        self.draw()
