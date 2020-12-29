# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 23:47:00 2020

@author: jcantero
"""

from random import randrange

class Presenter():

    def openDoor(doors):
        door = doors[randrange(len(doors))]
        door.setOpened()