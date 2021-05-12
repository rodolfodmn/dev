import pygame, random, sys
from pygame.locals import *

class Commands:

    def __init__(self):
        self.move = {
            'left': False,
            'right': False,
            'up': False,
            'down': False,
        }

    def terminate(self):
        pygame.quit()
        sys.exit()

    def waitForPlayerToPressKey(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: # pressing escape quits
                        terminate()
                    return

    def controls(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    reverseCheat = True
                if event.key == ord('x'):
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a'):
                    self.move["right"] = False
                    self.move["left"] = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    self.move["left"] = False
                    self.move["right"] = True
                if event.key == K_UP or event.key == ord('w'):
                    self.move["down"] = False
                    self.move["up"] = True
                if event.key == K_DOWN or event.key == ord('s'):
                    self.move["up"] = False
                    self.move["down"] = True

            if event.type == KEYUP:
                if event.key == ord('z'):
                    reverseCheat = False
                    score = 0
                if event.key == ord('x'):
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == ord('a'):
                    self.move["left"] = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    self.move["right"] = False
                if event.key == K_UP or event.key == ord('w'):
                    self.move["up"] = False
                if event.key == K_DOWN or event.key == ord('s'):
                    self.move["down"] = False


            if event.type == MOUSEMOTION:
                playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)
