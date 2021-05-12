import pygame, random, sys
from pygame.locals import *
from commands import Commands
from baddie import Baddie
from player import Player

class Screen(object):
    def __init__(self, width, height, background, fps, textColor):
        self.width = width
        self.height = height
        self.background = background
        self.fps = fps
        self.textColor = textColor
        self.windowSurface = pygame.display.set_mode((width, height))
        self.commands = Commands()
        self.baddies = Baddie()

    def to_string(self):
        print("{} {} {} {} {}".format(
            self.width, self.height, self.background, 
            self.fps, self.text
        ))

    def to_string(self):
        print("{} {} {} {} {}".format(
            self.width, self.height, self.background, 
            self.fps, self.text
        ))

    def start(self):
        pygame.init()
        mainClock = pygame.time.Clock()
        pygame.display.set_caption('Dodger')
        pygame.mouse.set_visible(False)

        self.drawText('Dodger', (self.width / 3), (self.height / 3))
        self.drawText('Press key to start.', (self.width/ 3) - 30, (self.height / 3) + 50)
        pygame.display.update()
        self.commands.waitForPlayerToPressKey()

        player = Player()
        baddies = []
        score = 0
        reverseCheat = slowCheat = False
        baddieAddCounter = 0
        pygame.mixer.music.play(-1, 0.0)

    def drawText(self, text, x, y):
        font = pygame.font.SysFont(None, 48)
        textobj = font.render(text, 1, self.textColor)
        textrect = textobj.get_rect()
        textrect = topleft = (x, y)
        self.windowSurface.blit(textobj, textrect)

    def render_loop(self):
        while True:
            score += 1





