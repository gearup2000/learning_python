import random as rnd
import math
import pygame

from my_colors import *

FPS = 20
GRAVITY_ACCELERATION = 9.8 # the earth gravity
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600


class Cannon:
    max_velocity = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shell_num None # TODO: the left shells
        self.direction = math.pi / 4

class Shell:
    standard_radius = 25

    def __init__(self, x, y, Vx, Vy):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vx
        self.r = Shell.standard_radius

    def move(self, dt):
        """
        Moves the shells depending of its kinetic characteristics
        :param self:
        :param dt:
        :return:
        """

class Target:
    standard_radius = 15

    def __init__(self, x, y, Vx, Vy):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vx
        self.r = Target.standard_radius
        self.color = COLORS[rnd.randint(0, len(COLORS))]

class Bomb:
    pass

def ClickDurationMeter:
    def __init__(self, button_number, delegated_handler):
        self._is_button_pushed = False
        self._timer = 0
        self.handler = delegated_handler

        def click_start(self, event):
            assert nit self._is_button_pushed = True
            self._timer = pygame.time.get_ticks()

        def click_end(self, event):

class WeaponWidgets:
    global balss, bullet
    bullet += 1
    self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
    new_ball.vx = self.f2_power * math.cos(self.an)
    new_ball.vy = - self.f2_power * math.sin(self.an)
    balls += [new_ball]

    self.f2_on = 0
    self.f2_power = 10

    def power_up(self):
        if self._on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill ='black')




