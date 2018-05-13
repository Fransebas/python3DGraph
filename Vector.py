from Geometry.Cone import *
from Drawable import *
import VBOGL

class Vector(Drawable):

    def __init__(self, end, start = [0,0,0]):
        super().__init__()

        self.end = end
        self.start = start
        self.vertex = [self.start, self.end]
        self.cone = Cone(0.3, 0.1, 12)
        self.shader = self.cone.shader

        self.isDefined = True

        self.__build__()

    def setRotation(self, abg):
        super().setRotation(abg)
        self.cone.setRotation(abg)

    def setAalpha(self, a):
        super().setAalpha(a)
        self.cone.setAalpha(a)

    def setBeta(self, b):
        super().setBeta(b)
        self.cone.setBeta(b)

    def setGama(self, c):
        super().setGama(c)
        self.cone.setGama(c)

    def rotAalpha(self, a):
        super().rotAalpha(a)
        self.cone.rotAalpha(a)

    def rotBeta(self, b):
        super().rotBeta(b)
        self.cone.rotBeta(b)

    def rotGama(self, c):
        super().rotGama(c)
        self.cone.rotGama(c)

    def setV(self, V):
        super().setV(V)
        self.cone.setV(V)

    def __build__(self):
        self.vbo = VBOGL.VBOGL(self.vertex,GL_LINES)
        self.cone.setXYZ(self.end)

        s = np.array(self.start)
        e = np.array(self.end)
        v = e - s

        if not np.all(np.abs(v) > 0.001):
            self.isDefined = False
            return

        v = v / np.linalg.norm(v)
        u = [ math.asin(a) for a in v ]

        abg = [u[2], 0, -u[0]]
        self.cone.setRotation(abg)

    def draw(self):
        if self.isDefined:
            if self.shader:
                self.shader.use()
                super().writeMatrixs(self.shader)

            self.vbo.draw()

            self.cone.draw()

