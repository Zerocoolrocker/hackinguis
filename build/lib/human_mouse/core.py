#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from random import randint
import math

from autopy_mouse.mouse import (
    move, click, get_pos,
    LEFT_BUTTON,
    RIGHT_BUTTON,
    CENTER_BUTTON
)

class HumanMouse:
    """ 
    Main class for human mouse performance.
    Before clicks moves to point.

    :param mouse_speed: Mouse velocity
        (optional, default == 18)
    :type mouse_speed: int/float

    :param gravity: If the number is larger, 
        grater uniformity of movement
        (optional, default == 60)
    :type gravity: inf/float

    :param wind: aleatority of movement
        (optional, default == 60)
    :type wind: int/float

    :param target_error: Error in target
        objetive (optional, default == 500)
        before achieve it without error
    :type target_error: int/float
    """
    def __init__(self, mouse_speed=18, gravity=60, 
                 wind=60, target_error=500):
        self.mouseSpeed = mouse_speed
        self.gravity = gravity
        self.wind = wind
        self.targetError = target_error

    def move(self, x, y):
        """Human mouse movement """
        startCoords = get_pos()
        coordsAndDelay = self._calcCoordsAndDelay(startCoords,
                                                  (x, y))
        for x, y, delay in coordsAndDelay:
            move(int(x), int(y))
            sleep(delay/1000)

    def click(self, x, y, button=LEFT_BUTTON,
              clicks=1, interval=0):
        """Perform a number of clicks after 
        human mouse movement

        :param button: Mouse button to use
            on the click. Valid types:
            (1, 2, 3, 'left', 'right', 'middle')
            (optional, default == 1)
        :type button: int/str

        :param clicks: Number of clicks
            (optional, default == 1)
        :type clicks: int

        :param interval: Time for sleep
            between clicks
            (optional, default == 0)
        :type interval: int/float
        """
        self.move(x, y)

        for c in range(clicks):
            click(button)
            if clicks > 1 and interval > 0:
                sleep(interval)

    def double_click(self, x, y, pause=.1, **kwargs):
        """Perform a classic double click
        after human mouse movement

        :param pause: Time to sleep between
            first and second click
            (optional, default == .1)
        :type pause: int/float
        """
        self.move(x, y)
        click(x, y, **kwargs)
        sleep(pause)
        click(x, y, **kwargs)
        
    def _calcCoordsAndDelay(self, startCoords, endCoords):
        """Internal function for calculate
        coordinates and delay to perform
        human mouse movement"""
        
        veloX, veloY = (0, 0)
        coordsAndDelay = []
        xs, ys = startCoords
        xe, ye = endCoords
        totalDist = math.hypot(xs - xe, ys - ye)

        self._windX = 0
        self._windY = 0

        while True:
            veloX, veloY = self._calcVelocity((xs, ys), (xe, ye), veloX, veloY, totalDist)
            xs += veloX
            ys += veloY

            w = round(max(randint(0, max(0, round(100/self.mouseSpeed)-1))*6, 5)*0.9)
            coordsAndDelay.append(( xs, ys, w ))

            if math.hypot(xs - xe, ys - ye) < 1:
                break

        if round(xe) != round(xs) or round(ye) != round(ys):
            coordsAndDelay.append(( round(xe), round(ye), 0 ))

        return coordsAndDelay

    def _calcVelocity(self, curCoords, endCoords, veloX, veloY, totalDist):
        xs, ys = curCoords
        xe, ye = endCoords
        dist = math.hypot(xs - xe, ys - ye)
        self.wind = max(min(self.wind, dist), 1)

        maxStep = None
        D = max(min(round(round(totalDist)*0.3)/7, 25), 5)
        rCnc = randint(0, 5)

        if rCnc == 1:
            D = 2

        if D <= round(dist):
            maxStep = D
        else:
            maxStep = round(dist)

        if dist >= self.targetError:
            self._windX = self._windX / math.sqrt(3) + (randint(0, round(self.wind) * 2) - self.wind) / math.sqrt(5)
            self._windY = self._windY / math.sqrt(3) + (randint(0, round(self.wind) * 2) - self.wind) / math.sqrt(5)
        else:
            self._windX = self._windX / math.sqrt(2)
            self._windY = self._windY / math.sqrt(2)

        veloX = veloX + self._windX
        veloY = veloY + self._windY
        
        if(dist != 0):
            veloX = veloX + self.gravity * (xe - xs) / dist
            veloY = veloY + self.gravity * (ye - ys) / dist

        if math.hypot(veloX, veloY) > maxStep:
            randomDist = maxStep / 2.0 + randint(0, math.floor(round(maxStep) / 2))
            veloMag = math.sqrt(veloX * veloX + veloY * veloY)
            veloX = (veloX / veloMag) * randomDist
            veloY = (veloY / veloMag) * randomDist

        return (veloX, veloY)
