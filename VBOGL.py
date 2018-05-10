from OpenGL.arrays import vbo
from OpenGL.GL import *
import numpy as np

class VBOGL():

    def __init__(self, vertex):
        self.vertex = vertex
        self.vbo = vbo.VBO(
            np.array(self.vertex), dtype=np.float32
        )

    def draw(self):
        self.vbo.bind()

        glEnableClientState(GL_VERTEX_ARRAY)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        self.vbo.unbind()
        glDisableClientState(GL_VERTEX_ARRAY)