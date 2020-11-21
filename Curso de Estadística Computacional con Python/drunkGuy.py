#this files crear a class that makes drunk Guys 

import random

class DrunkGuy:
    def __init__(self,name):
        self.name = name

class TraditionalDrunk(DrunkGuy):
    def __init__(self,name):
        super().__init__(name)

    def walkPatern(self):
        return random.choice([(0,1),(1,0),(0,-1),(-1,0)])

class crazyDrunk(DrunkGuy):
    def __init__(self,name):
        super().__init__(name)

    def walkPatern(self):
        return random.choice([(0,2),(3,0),(0,-2),(-2,0)])