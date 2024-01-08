import pygame as pg
from conf import *
from player import Player
from enemy import Enemy
from time import sleep


class Game:
    def __init__(self, main):
        self.main = main
        self.player = Player(self)
        self.enemys = list()
        self.score = 0

        # Events
        self.spawn_enemy = pg.USEREVENT + 1
        pg.time.set_timer(self.spawn_enemy, 1500)

        self.main.game_background_sound.play(-1)

    def delete(self):
        del self.spawn_enemy
        self.main.game_background_sound.stop()

    def event_handler(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.main.layers[-1].delete()
                self.main.layers.pop()
                self.main.menu_background_sound.play(-1)
                return
        if event.type == self.spawn_enemy:
            if len(self.enemys) < 20:
                self.enemys.append(Enemy(self))

    def update(self):
        self.player.update()

        for enemy in self.enemys:
            enemy.update()
            for bullet in self.player.bullets:
                distance = (enemy.pos_x - bullet.pos_x) ** 2 + (enemy.pos_y - bullet.pos_y) ** 2
                if distance < 800:
                    self.enemys.remove(enemy)
                    self.player.bullets.remove(bullet)
                    self.main.enemy_death_sound.play()
                    self.score += 1

            # Game over
            distance = (enemy.pos_x - self.player.pos_x) ** 2 + (enemy.pos_y - self.player.pos_y) ** 2
            if distance < 2500:
                self.main.enemy_death_sound.play()
                sleep(2)
                self.delete()
                self.main.layers.pop()
                self.main.menu_background_sound.play(-1)

    def draw(self):
        self.player.draw()

        for enemy in self.enemys:
            enemy.draw()

        score = self.main.font.render(f"Score: {self.score}", True, WHITE)
        score_pos = score.get_rect(center=((WIDTH // 2), 20))
        self.main.screen.blit(score, score_pos)
