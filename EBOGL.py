from OpenGL.arrays import vbo
from OpenGL.GL import *
import numpy as np

class EBOGL():

    def __init__(self, vertex, index, textCoords = []):
        self.vertex = np.array(vertex, dtype=np.float32)
        self.index = np.array(index, dtype=np.uint32)
        self.coords = np.array(textCoords, dtype=np.float32)

        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)
        self.ebo = glGenBuffers(1)

        self.vertexIndex = 0
        self.colorIndex = 1
        self.coordsIndex = 2

        self.bind()
        glEnableVertexAttribArray(0)

        #glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertex.nbytes, self.vertex, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        #glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.index.nbytes ,self.index, GL_STATIC_DRAW)



        """n = 0
        n += self.storeMemory(self.vertex, n, self.vertexIndex)

        if len(self.coords) > 0:
            n += self.storeMemory(self.coords, n, self.coordsIndex, dataSize=2)"""


    def storeMemory(self, data, stride, i, dataSize = 3, type = GL_FLOAT):
        glBufferSubData(GL_ARRAY_BUFFER, stride, data.nbytes, data)
        glVertexAttribPointer(i, dataSize, type, GL_FALSE, 0, ctypes.c_void_p(stride))
        return data.nbytes

    def bind(self):
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)


    def draw(self):
        glEnableVertexAttribArray(0)

        self.bind()

        glDrawElements(GL_TRIANGLES, len(self.index), GL_UNSIGNED_INT, ctypes.c_void_p(0))