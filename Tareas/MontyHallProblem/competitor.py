# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 23:30:00 2020

@author: jcantero
"""

from random import randrange

class Competitor():

    def chooseDoor(doors):
        door = doors[randrange(len(doors))]
        door.setSelected()

    def changeDoor(doors):
        for door in doors:
            if door.isSelected():
                door.unSelected()
            else:
                door.setSelected()
