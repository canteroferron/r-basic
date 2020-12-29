# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:57:54 2020

@author: jcantero
"""

from doors_factory import DoorsFactory
from competitor import Competitor
from presenter import Presenter 
from doors_cache import DoorsCache

N = 10000
withDoorChange = [True, False]

for witchChange in withDoorChange:
    countWin = 0
    for i in range (0, N):
        doorsCache = DoorsCache(DoorsFactory.build())
        Competitor.chooseDoor(doorsCache.getDoors())
        Presenter.openDoor(doorsCache.getDoorsWithoutPrizeAndNotSelected())

        #print(doorsCache.getDoors())
        if witchChange:
            Competitor.changeDoor(doorsCache.getDoorsNotOpened())
        #print(doorsCache.getDoors())

        if (doorsCache.getDoorSelected().havePrize()):
            countWin = countWin +1

    print(f"El numero de aciertos es {countWin} sobre {N} intentos con cambio a {witchChange}")
