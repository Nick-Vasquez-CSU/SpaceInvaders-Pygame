import pygame as pg
from vector import Vector
from pygame.sprite import Sprite, Group
from copy import copy
from random import randint

# from alien import Alien
# from stats import Stats


class ALasers:

    def __init__(self, game):
        self.game = game
        self.stats = game.stats
        self.ship = game.ship
        self.lasers = Group()

    def add(self, laser): self.lasers.add(laser)
    def empty(self): self.lasers.empty()
    def fire(self):
      se_laser = pg.mixer.Sound("laser_ship.mp3")
      new_laser = Laser(self.game)
      pg.mixer.Sound.play(se_laser)
      self.lasers.add(new_laser)

    def update(self):
        for laser in self.lasers.copy():
            if laser.rect.bottom <= 0: self.lasers.remove(laser)

        for laser in self.lasers.copy():
            if pg.sprite.spritecollideany(self.ship, self.lasers):
                self.ship.hit()
                laser.kill()
  #      if self.alien_fleet.length() == 0:
   #         self.stats.level_up()
    #        self.game.restart()
            
        for laser in self.lasers:
            laser.update()

    def draw(self):
        for laser in self.lasers:
            laser.draw()


class Laser(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.w, self.h = self.settings.laser_width, self.settings.laser_height
        self.ship = game.ship
        self.fleet = game.alien_fleet

        self.rect = pg.Rect(0, 0, self.w, self.h)
        self.center = Vector(randint(0,1200), 0)
        # print(f'center is at {self.center}')
        # self.color = self.settings.laser_color
        tu = 50, 255
        self.color = randint(*tu), randint(*tu), randint(*tu)
        self.v = Vector(0, 1) * self.settings.laser_speed_factor

    def update(self):
        self.center += self.v
        self.rect.x, self.rect.y = self.center.x, self.center.y

    def draw(self): pg.draw.rect(self.screen, color=self.color, rect=self.rect)