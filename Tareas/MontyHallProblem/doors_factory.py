# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 10:51:57 2020

@author: jcantero
"""

from random import randrange
from door import Door

class DoorsFactory:
    
    def build():
        prizes = [0, 0, 1]
        
        doors = []
        
        for i in range(0, 3):
            prize = prizes[randrange(len(prizes))]
            
            doors.append(Door(f"Door{i + 1}", prize, 0, 0))
            
            prizes.remove(prize)
            
        return doors
