from VBOGL import *
from Drawable import *
from Shaders import  *
from Function import *

class Parametric(Drawable):

    def __init__(self, strf, interval, steps):
        super().__init__()
        self.shader = Shader()
        self.shader.addFragment("shaders/fragmentParametric.frag")
        self.shader.addVertex("shaders/fragmentParametric.vert")
        self.shader.compile()
        self.f = Function(strf, type=Function.Types.PARAMETRIC)
        self.interval = interval
        self.steps = steps
        self.vertex = []

        self.__build__()

    def getFunction(self):
        return self.f

    def __build__(self):

        self.d = (self.interval[1] - self.interval[0]) / float (self.steps)


        for i in range(self.steps):
            self.vertex.append(self.f.eval(i * self.d + self.interval[0]))


        self.vbo = VBOGL(self.vertex, GL_LINE_STRIP)


    def draw(self):
        if self.shader:
            self.shader.use()
            super().writeMatrixs(self.shader)

        self.vbo.draw()