import pygame as pg
import sys
from doc.conf import *
from levels.menu import Menu


class Main:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        pg.display.set_caption("Game")
        self.show_fps = True
        self.pipe = False

        self.font = pg.font.Font(pg.font.get_default_font(), 18)
        self.font2 = pg.font.Font(pg.font.get_default_font(), 136)
        self.font3 = pg.font.Font(pg.font.get_default_font(), 32)

        # Events
        self.spawn_enemy = pg.USEREVENT + 1
        pg.time.set_timer(self.spawn_enemy, 1500)

        # Sounds
        self.falling_pipe_sound = pg.mixer.Sound("./assets/audio/falling-pipe.mp3")
        self.falling_pipe_sound.set_volume(0.75)
        self.gun_sound = pg.mixer.Sound("./assets/audio/gun-fire-sound.mp3")
        self.gun_sound.set_volume(0.65)
        self.enemy_death_sound = pg.mixer.Sound("./assets/audio/enemy-death.wav")
        self.enemy_death_sound.set_volume(0.75)
        self.reload_sound = pg.mixer.Sound("./assets/audio/reload.mp3")
        self.reload_sound.set_volume(0.75)
        self.game_background_sound = pg.mixer.Sound("./assets/audio/game-background.mp3")
        self.game_background_sound.set_volume(0.25)
        self.menu_background_sound = pg.mixer.Sound("./assets/audio/menu-background.mp3")
        self.menu_background_sound.set_volume(0.5)

        # Layers
        self.layers = list()
        self.layers.append(Menu(self))

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game_over()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_INSERT:
                    self.show_fps = False if self.show_fps else True
                if event.key == pg.K_p:
                    self.pipe = False if self.pipe else True

            self.layers[-1].event_handler(event)

    def update(self):
        self.clock.tick(120)
        self.layers[-1].update()

    def draw(self):
        self.screen.fill(BLACK)

        self.layers[-1].draw()

        if self.show_fps:
            fps = self.font.render(f"{self.clock.get_fps():.0f}", True, WHITE)
            self.screen.blit(fps, (10, 10))

    def run(self):
        while True:
            self.event_handler()
            self.update()
            self.draw()
            pg.display.update()

    def game_over(self):
        pg.quit()
        sys.exit(0)


if __name__ == '__main__':
    game = Main()
    game.run()
