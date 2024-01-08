import pygame as pg
from time import time
from doc.conf import *
from levels.game import Game


class Menu:
    def __init__(self, main):
        self.main = main

        # Texts
        self.title_text = self.main.font2.render("THE FPS", True, RED)
        self.title_rect = self.title_text.get_rect(center=(WIDTH // 2, 175))
        self.play_text = self.main.font3.render("Press ENTER to Play", True, GREEN)
        self.play_rect = self.play_text.get_rect(center=(WIDTH // 2, HEIGHT - 100))
        self.controls_text = self.main.font.render("WASD to Move, SPACE to shoot, R to reload, ESC to exit, Good Luck!", True, WHITE)
        self.controls_rect = self.controls_text.get_rect(bottomleft=(10, HEIGHT - 10))

        self.time = time()
        self.toggle = True

        self.main.menu_background_sound.play(-1)

    def delete(self): ...

    def event_handler(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.main.layers.append(Game(self.main))
                self.main.menu_background_sound.stop()
            if event.key == pg.K_ESCAPE:
                self.main.game_over()

    def update(self):
        if self.play_rect.collidepoint(pg.mouse.get_pos()):
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
            if pg.mouse.get_pressed()[0]:
                self.main.layers.append(Game(self.main))
                self.main.menu_background_sound.stop()
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        else:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)

        if time() - self.time > 0.5:
            self.toggle = False if self.toggle else True
            self.time = time()

    def draw(self):
        self.main.screen.blit(self.title_text, self.title_rect)
        if self.toggle:
            self.main.screen.blit(self.play_text, self.play_rect)
        self.main.screen.blit(self.controls_text, self.controls_rect)
