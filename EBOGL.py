from OpenGL.arrays import vbo
from OpenGL.GL import *
import numpy as np

class EBOGL():

    def __init__(self, vertex, index,textCoords = [], normals = []):
        self.vertex = np.array(vertex, dtype=np.float32)
        self.index = np.array(index, dtype=np.uint32)
        self.coords = np.array(textCoords, dtype=np.float32)
        self.normals = np.array(normals, dtype=np.float32)

        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)
        self.ebo = glGenBuffers(1)

        self.vertexIndex = 0
        self.coordsIndex = 1
        self.normalIndex = 2

        self.bind()

        glBufferData(GL_ARRAY_BUFFER,
                     self.vertex.nbytes + self.coords.nbytes + self.normals.nbytes,
                     None,
                     GL_STATIC_DRAW)
        #glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        n = 0
        n += self.storeMemory(data=self.vertex,
                              stride=n,
                              i=self.vertexIndex)

        if len(self.coords) > 0:
            n += self.storeMemory(data=self.coords,
                                  stride=n,
                                  i=self.coordsIndex,
                                  dataSize=2)

        if len(self.normals) > 0:
            n += self.storeMemory(data=self.normals,
                                  stride=n,
                                  i=self.normalIndex)

        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.index.nbytes, self.index, GL_STATIC_DRAW)


    def storeMemory(self, data, stride, i, dataSize = 3, type = GL_FLOAT):
        #glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferSubData(GL_ARRAY_BUFFER, stride, data)
        glVertexAttribPointer(i, dataSize, type, GL_FALSE, 0, ctypes.c_void_p(stride))
        return data.nbytes

    def bind(self):
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)

        glEnableVertexAttribArray(self.vertexIndex)
        if len(self.coords) > 0:
            glEnableVertexAttribArray(self.coordsIndex)

        if len(self.normals) > 0:
            glEnableVertexAttribArray(self.normalIndex)


    def draw(self):
        self.bind()

        glDrawElements(GL_TRIANGLES, len(self.index), GL_UNSIGNED_INT, ctypes.c_void_p(0))