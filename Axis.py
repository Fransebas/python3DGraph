from Drawable import  *
from VBOGL import *
from Shaders import  *

class Axis(Drawable):

    def __init__(self):
        super().__init__()

        self.shader = Shader()
        self.shader.addFragment("shaders/fragmentAxis.frag")
        self.shader.addVertex("shaders/fragmentAxis.vert")
        self.shader.compile()

        self.vertex = [
            0.0, 0.0, -1.0,
            0.0, 0.0, 1.0,
            -1.0, 0.0, 0.0,
            1.0, 0.0, 0.0,
            0.0, -1.0, 0.0,
            0.0, 1.0, 0.0
                       ]

        self.__build__()

    def __build__(self):
        self.vbo = VBOGL(self.vertex, GL_LINES)

    def draw(self):
        self.__generateMatrix__()
        if self.shader:
            self.shader.use()
            super().writeMatrixs(self.shader)

        self.vbo.draw()