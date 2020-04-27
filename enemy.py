import random

import astarpy

class enemyC():
    def __init__(self, x, y, floor):
        self.x = x
        self.y = y
        self.floor = floor
        self.hits = floor
        self.damage = floor
        self.show = True

    def showEnemy(self, display):
        if(self.show):
            display[self.y][self.x] = 8

    def replaceChar(self, display):
        if(self.show):
            display[self.y][self.x] = 0

    def checkHit(self, display):
        if(self.show):
            if(display[self.y][self.x + 1] == 3 or display[self.y][self.x - 1] == 3 or display[self.y - 1][self.x] == 3 or display[self.y + 1][self.x] == 3):
                self.hits = self.hits - 1

            if(self.hits == 0):
                self.show = False
                return self.floor * 10

            else:
                return 0

        else:
            return 0

    def checkPlayer(self, playerx, playery):
        if(self.show):
            if(self.x == playerx and self.y == playery):
                self.show = False
                return self.damage

            else:
                return 0

        else:
            return 0

    def moveEnemy(self, display, walls, playerx, playery):
        if(self.show):

            start = [playerx, playery]
            end = [self.x, self.y]

            path = []

            if(abs(self.x - playerx) < 15 and abs(self.y - playery) < 15):
                path = astarpy.astar(start, end, walls)

            if(path != []):
                self.x = path[0][0]
                self.y = path[0][1]
