from Vector import *
from enum import Enum

from Drawable import *

from Function import *

class VectorField(Drawable):

    class Types(Enum):
        COLORED = 1
        SIZED = 2


    def __init__(self, strf, type = Types.SIZED):
        super().__init__()
        self.f = Function(strf, type=Function.Types.VECTOR)
        self.type = type
        self.vectors = []
        self.xRange = 5
        self.yRange = 5
        self.zRange = 5
        self.scale = 5


        #if self.type == Types.COLORED:
        #    raise NotImplementedError

        self.__build__()

    def __build__(self):
        scaleX = self.scale/self.xRange
        scaleY = self.scale/self.yRange
        scaleZ = self.scale/self.zRange

        for i in range(0,self.xRange):
            for j in range(0, self.yRange):
                for k in range(0, self.zRange):
                    x = scaleX*i - scaleX*self.xRange/2.0
                    y = scaleY*j - scaleY*self.yRange/2.0
                    z = scaleZ*k - scaleZ*self.zRange/2.0
                    end = self.f.eval(x,y,z)
                    self.vectors.append(Vector(start=[x,y,z], end=end))

    def getFunction(self):
        return self.f

    def setXYZ(self,xyz):
        super().setXYZ(xyz)
        for v in self.vectors:
            v.setXYZ(xyz)

    def setX(self, x):
        super().setX(x)
        for v in self.vectors:
            v.setX(x)

    def setY(self, y):
        super().setX(y)
        for v in self.vectors:
            v.setX(y)

    def setZ(self, z):
        super().setZ(z)
        for v in self.vectors:
            v.setZ(z)

    def setRotation(self, abg):
        super().setRotation(abg)
        for v in self.vectors:
            v.setRotation(abg)

    def setAalpha(self, a):
        super().setAalpha(a)
        for v in self.vectors:
            v.setAalpha(a)

    def setBeta(self, b):
        super().setBeta(b)
        for v in self.vectors:
            v.setBeta(b)

    def setGama(self, c):
        super().setGama(c)
        for v in self.vectors:
            v.setGama(c)


    def rotAalpha(self, a):
        super().rotAalpha(a)
        for v in self.vectors:
            v.rotAalpha(a)

    def rotBeta(self, b):
        super().rotBeta(b)
        for v in self.vectors:
            v.rotBeta(b)

    def rotGama(self, c):
        super().rotGama(c)
        for v in self.vectors:
            v.rotGama(c)

    def setV(self, V):
        super().setV(V)
        for v in self.vectors:
            v.setV(V)

    def draw(self):
        for v in self.vectors:
            v.draw()
