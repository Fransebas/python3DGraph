from OpenGL.arrays import vbo
from OpenGL.GL import *
import numpy as np

class VBOGL():

    def __init__(self, vertex, drawMode= GL_TRIANGLES):
        self.vertex = np.array(vertex, dtype=np.float32)
        self.drawMode = drawMode
        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)

        self.bind()

        glBufferData(GL_ARRAY_BUFFER, self.vertex.nbytes, self.vertex, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

    def bind(self):
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)

        glEnableVertexAttribArray(0)

    def draw(self):
        self.bind()
        glDrawArrays(self.drawMode, 0, len(self.vertex))