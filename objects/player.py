import pygame as pg
from doc.conf import *
from objects.bullet import Bullet
import math


class Player:
    def __init__(self,  game):
        self.game = game
        self.pos_x = WIDTH // 2
        self.pos_y = HEIGHT // 2
        self.size = 20
        self.ang = 0
        self.ac_x = 0
        self.ac_y = 0
        self.ac_ang = 0
        self.bullets: list[Bullet] = list()
        self.using_gun = False
        self.ammo = 4

    def update(self):
        keys = pg.key.get_pressed()

        # Vertical moviment
        if keys[pg.K_w]:
            self.ac_y -= 0.05 if self.ac_y > -2 else 0
        elif keys[pg.K_s]:
            self.ac_y += 0.05 if self.ac_y < 2 else 0
        else:
            if abs(self.ac_y) < 0.2:
                self.ac_y = 0
            elif self.ac_y > 0:
                self.ac_y -= 0.05
            elif self.ac_y < 0:
                self.ac_y += 0.05

        # Horizontal moviment
        if keys[pg.K_a]:
            self.ac_x -= 0.05 if self.ac_x > -2 else 0
        elif keys[pg.K_d]:
            self.ac_x += 0.05 if self.ac_x < 2 else 0
        else:
            if abs(self.ac_x) < 0.2:
                self.ac_x = 0
            elif self.ac_x > 0:
                self.ac_x -= 0.05
            elif self.ac_x < 0:
                self.ac_x += 0.05

        # Angular moviment
        if keys[pg.K_RIGHT]:
            self.ac_ang -= 0.09 if self.ac_ang > -2 else 0
        elif keys[pg.K_LEFT]:
            self.ac_ang += 0.09 if self.ac_ang < 2 else 0
        else:
            if abs(self.ac_ang) < 0.2:
                self.ac_ang = 0
            elif self.ac_ang > 0:
                self.ac_ang -= 0.09
            elif self.ac_ang < 0:
                self.ac_ang += 0.09

        # Shooting
        if keys[pg.K_SPACE] and not self.using_gun:
            self.using_gun = True
            if self.ammo > 0:
                self.ammo -= 1
                self.game.main.gun_sound.play()
                self.bullets.append(Bullet(self.game,
                                           self.pos_x + 40 * math.sin(math.radians(self.ang)),
                                           self.pos_y + 40 * math.cos(math.radians(self.ang)),
                                           self.ang))
                self.ac_x += 2 * -math.sin(math.radians(self.ang))
                self.ac_y += 2 * -math.cos(math.radians(self.ang))
        elif keys[pg.K_r] and not self.using_gun:
            self.using_gun = True
            if self.ammo < 4:
                self.ammo = 4
                self.game.main.reload_sound.play()
        elif not keys[pg.K_SPACE] and not keys[pg.K_r]:
            self.using_gun = False

        # Updating pos and ang
        self.pos_y += self.ac_y
        self.pos_x += self.ac_x
        self.ang += self.ac_ang

        # Correcting ang
        if self.ang > 359:
            self.ang -= 360
        elif self.ang < 0:
            self.ang += 360

        # Updating each bullet
        for bullet in self.bullets:
            bullet.update()
            if (bullet.pos_x < -100 or
                    bullet.pos_x > WIDTH + 100 or
                    bullet.pos_y < -100 or
                    bullet.pos_y > HEIGHT + 100):
                self.bullets.remove(bullet)
                if self.game.main.pipe:
                    self.game.main.falling_pipe_sound.play()

    def draw(self):
        pg.draw.circle(self.game.main.screen, WHITE, (self.pos_x, self.pos_y), self.size, 5)
        pg.draw.line(self.game.main.screen, WHITE, (self.pos_x, self.pos_y),
                     (self.pos_x + 40 * math.sin(math.radians(self.ang)),
                      self.pos_y + 40 * math.cos(math.radians(self.ang))),
                     5)
        for bullet in self.bullets:
            bullet.draw()
        ammo_left = self.game.main.font.render(f"Ammo: {self.ammo}", True, WHITE)
        ammo_left_pos = ammo_left.get_rect(topright=(WIDTH - 10, 10))
        self.game.main.screen.blit(ammo_left, ammo_left_pos)
