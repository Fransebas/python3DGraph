from VBOGL import *
from Drawable import *
from Shaders import  *

class Parametric(Drawable):

    def __init__(self, f, interval, steps):
        super().__init__()
        self.shader = Shader()
        self.shader.addFragment("shaders/fragmentParametric.frag")
        self.shader.addVertex("shaders/fragmentParametric.vert")
        self.shader.compile()
        self.f = f
        self.interval = interval
        self.steps = steps
        self.vertex = []

        self.__build__()

    def __build__(self):

        self.d = (self.interval[1] - self.interval[0]) / float (self.steps)


        for i in range(self.steps):
            self.vertex.append(self.f(i * self.d + self.interval[0]))


        self.vbo = VBOGL(self.vertex, GL_LINE_STRIP)


    def draw(self):
        self.__generateMatrix__()
        if self.shader:
            self.shader.use()
            super().writeMatrixs(self.shader)

        self.vbo.draw()