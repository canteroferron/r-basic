# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:59:38 2020

@author: jcantero
"""

class Door(): 
    def __init__(self, name, prize, selected, opened):
        self.name = name
        self.prize = prize
        self.selected = selected
        self.opened = opened


    def setSelected(self):
        self.selected = 1

    def unSelected(self):
        self.selected = 0

    def isSelected(self):
        return self.selected == 1

    def setOpened(self):
        self.opened = 1

    def isOpened(self):
        return self.opened == 1

    def havePrize(self):
        return self.prize == 1

    def __str__(self):
        return f"Door[name={self.name}, prize={self.prize}, selected={self.selected}, opened={self.opened}]"
    
    def __repr__(self):
        return f"Door[name={self.name}, prize={self.prize}, selected={self.selected}, opened={self.opened}]"