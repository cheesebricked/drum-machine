import pygame
import settings
from render import box_list
from saves import saves, bpms

pygame.mixer.init()
pygame.font.init()

box_width = ((settings.SCREEN_WIDTH / settings.BEAT_LENGTH) - (settings.SCREEN_WIDTH / (settings.BEAT_LENGTH * 5)))
indicator_pos = (settings.LABEL_LENGTH)
box_height = settings.BOX_HEIGHT
label_font_large = pygame.font.SysFont("Arial", 45)
label_font = pygame.font.SysFont("Arial", 30)
label_font_small = pygame.font.SysFont("Arial", 15)

BPM = 120
TICK_BEAT = (int(60000 / (BPM * (settings.SUBDIVISION / 4))))

class BOX():
    def __init__(self, x, y, screen, sample, outline_color):
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
        self.grey = (200, 200, 200)
        self.green = (0, 200, 0)
        self.outline = outline_color
        self.outline_color = self.outline

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)
        pygame.draw.rect(self.surface, self.outline_color, self.rect, 5)

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
            self.outline_color = self.outline
        if indicator_pos == self.rect.x:
            self.outline_color = self.green

    def draw_label_text(self, text):
        self.label = label_font.render(text, True, (200,200,200))
        self.surface.blit(self.label, ((settings.LABEL_LENGTH / 10), (self.y + (box_height / 10))))

    def draw_label(self):
        pygame.draw.rect(self.surface, (0, 0, 0), self.label_rect)
        pygame.draw.rect(self.surface, (200,200,200), self.label_rect, 5)
        self.draw_label_text(self.sound)

    def change_state(self, state_input):
        self.active = state_input

    def save_state(self):
        if self.active:
            return True
        else:
            return False

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
        if self.indicator.x < (settings.SCREEN_WIDTH - (box_width * 2)):
            self.count += 1
            self.indicator.x = (((settings.SCREEN_WIDTH - + settings.LABEL_LENGTH) * (self.count / (settings.BEAT_LENGTH))) + settings.LABEL_LENGTH)
            global indicator_pos
            indicator_pos = self.indicator.x

        else:
            self.indicator.x = (settings.LABEL_LENGTH)
            indicator_pos = self.indicator.x
            self.count = 0

    def run(self):
        #self.draw()
        pass

class Menu():
    def __init__(self, screen):
        self.y_pos = (settings.SCREEN_HEIGHT - settings.MENU_HEIGHT)
        self.surface = screen

        self.menu_rect = pygame.Rect(0, self.y_pos, settings.SCREEN_WIDTH, settings.MENU_HEIGHT)
        self.menu_color = (120, 120, 120)

        self.bpm_x = (settings.LABEL_LENGTH)
        self.bpm_y = (self.y_pos + (self.y_pos / 20))
        self.bpm_rect = pygame.Rect(self.bpm_x, self.bpm_y, 70, 60)

    def change_bpm(self, n):
        self.m_pos = pygame.mouse.get_pos()
        if self.bpm_rect.collidepoint(self.m_pos):
            global BPM
            global TICK_BEAT
            BPM += n
            TICK_BEAT = (int(60000 / (BPM * (settings.SUBDIVISION / 4))))

    def get_bpm(self):
        return BPM
    
    def draw_bg(self):
        pygame.draw.rect(self.surface, self.menu_color, self.menu_rect)

    def draw_bpm(self):
        self.bpm_text = label_font_large.render(str(BPM), True, self.menu_color)
        pygame.draw.rect(self.surface, (0,0,0), self.bpm_rect)
        self.surface.blit(self.bpm_text, (self.bpm_x, self.bpm_y))
    
    def run(self):
        self.draw_bg()
        self.draw_bpm()

class Saves():
    def __init__(self, x, y, num, screen, size):
        self.surface = screen
        self.y_pos = (settings.SCREEN_HEIGHT - settings.MENU_HEIGHT)
        self.x = x
        self.y = y

        self.size = size
        self.num = str(num)

        self.label = label_font.render(self.num, True, (120, 120, 120))
        self.save_rect = pygame.Rect(x, y, self.size, self.size)
    
    def save(self):
        if self.save_rect.collidepoint(pygame.mouse.get_pos()):
            for b in box_list:
                saves[self.num].append(b.save_state())
            bpms[self.num] = BPM
            print("saved!")
    
    def load(self):
        global BPM
        global TICK_BEAT
        if self.save_rect.collidepoint(pygame.mouse.get_pos()):
            for s in range(len(box_list)):
                box_list[(s - 1)].change_state(saves[self.num][(s-1)])
            BPM = bpms[self.num]
            TICK_BEAT = (int(60000 / (BPM * (settings.SUBDIVISION / 4))))
            print("loaded!")

    def draw(self):
        pygame.draw.rect(self.surface, (0,0,0), self.save_rect)
        self.surface.blit(self.label, (self.x, self.y))

    def run(self):
        self.draw()