import pygame as pg
from doc.conf import *
import math


class Bullet:
    def __init__(self, game, pos_x, pos_y, ang):
        self.game = game
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.ang = math.radians(ang)

    def update(self):
        self.pos_x += 5 * math.sin(self.ang)
        self.pos_y += 5 * math.cos(self.ang)

    def draw(self):
        pg.draw.circle(self.game.main.screen, GREEN, (self.pos_x, self.pos_y), 5)
