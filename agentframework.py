import random
class Agent(object):
    def __init__(self):
        self._y = random.randint(0,99)
        self._x = random.randint(0,99)
    def getx(self):
         return self._x
    def gety(self):
         return self._y
    
    def setx(self,x):
         self._x = x
    def sety(self,y):
         self._y = y
    
        
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100