# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 00:10:00 2020

@author: jcantero
"""

class DoorsCache():

    def __init__(self, doors):
        self.doors = doors

    def getDoors(self):
        return self.doors

    def getDoorsWithoutPrizeAndNotSelected(self):
        ret = []
        for door in self.doors:
            if not door.havePrize() and not door.isSelected():
                ret.append(door)
        return ret

    def getDoorsNotOpened(self):
        ret = []
        for door in self.doors:
            if not door.isOpened():
                ret.append(door)
        return ret

    def getDoorSelected(self):
        door = None

        i = 0
        while door == None:
            aux = self.doors[i]
            if aux.isSelected():
                door = self.doors[i]
            i = i + 1
        
        return door
