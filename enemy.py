import pygame as pg
from conf import *
from random import randint


class Enemy:
    def __init__(self, game):
        self.game = game
        self.pos_x = randint(0, 1) * (WIDTH + 200) - 100
        self.pos_y = randint(0, HEIGHT // 50) * 50
        self.speed = 1

    def update(self):
        if self.pos_x > self.game.player.pos_x:
            self.pos_x -= self.speed
        elif self.pos_x < self.game.player.pos_x:
            self.pos_x += self.speed
        if self.pos_y > self.game.player.pos_y:
            self.pos_y -= self.speed
        elif self.pos_y < self.game.player.pos_y:
            self.pos_y += self.speed

    def draw(self):
        pg.draw.circle(self.game.main.screen, RED, (self.pos_x, self.pos_y), 25)
