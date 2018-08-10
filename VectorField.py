from Vector import *
from enum import Enum

from Drawable import *

from Function import *
import numpy as np


class VectorField(Drawable):
    class Types(Enum):
        COLORED = 1
        SIZED = 2

    def __init__(self, strf, type=Types.SIZED):
        super().__init__()
        self.f = Function(strf, type=Function.Types.VECTOR)
        self.type = type
        self.vectors = []
        self.xRange = 7
        self.yRange = 7
        self.zRange = 7
        self.scale = 7
        self.maxsize = 0

        # if self.type == Types.COLORED:
        #    raise NotImplementedError

        self.__build__()

    def __build__(self):
        scaleX = self.scale / self.xRange
        scaleY = self.scale / self.yRange
        scaleZ = self.scale / self.zRange
        self.maxsize = -9999

        vectors = []

        for i in range(0, self.xRange):
            for j in range(0, self.yRange):
                for k in range(0, self.zRange):
                    x = scaleX * i - scaleX * self.xRange / 2.0
                    y = scaleY * j - scaleY * self.yRange / 2.0
                    z = scaleZ * k - scaleZ * self.zRange / 2.0
                    start = np.array((x, y, z), dtype=np.float32)
                    end = np.array(self.f.eval(x, y, z), dtype=np.float32)
                    size = np.linalg.norm(end - start)
                    vectors.append((start, end, size))
                    self.maxsize = max(self.maxsize, size)

        for start, end, size in vectors:
            color = np.array([size / self.maxsize, 0, 1 - size / self.maxsize], dtype=np.float)
            self.vectors.append(Vector(start=start, end=end, color=color))

    def getFunction(self):
        return self.f

    def setXYZ(self, xyz):
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
