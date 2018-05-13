from Drawable import *
import numpy as np
import math
import EBOGL
import Face

from Shaders import *

class Cone(Drawable):

    def __init__(self, height, rad, slices):
        super(Cone, self).__init__()

        self.shader = Shader()
        self.shader.addVertex("shaders/fragment.vert")
        self.shader.addFragment("shaders/fragmentCone.frag")
        self.shader.compile()

        self.height = height
        self.rad = rad
        self.slices = int(slices)
        self.vertex = []
        self.indexs = []
        self.normals = []

        self.__build__()


    def __build__(self):
        self.vertex.append([0,-self.height/2,0])
        self.vertex.append([0,self.height/2,0])

        d = (2.0*np.pi) / self.slices

        for i in range(self.slices):
            t = i*d
            x = self.rad*math.cos(t)
            y = -self.height/2
            z = self.rad*math.sin(t)
            self.vertex.append([x,y,z])
            self.normals.append([0,0,0])

        for i in range(self.slices):

            j = 2 + (i%self.slices)
            k = 2 + ((i+1)%self.slices)

            self.indexs.append(0)
            self.indexs.append(j)
            self.indexs.append(k)

            self.indexs.append(1)
            self.indexs.append(j)
            self.indexs.append(k)

            face = Face.Face(self.vertex[0], self.vertex[j], self.vertex[k])
            self.normals[0] = face.getNormal()
            self.normals[j] = face.getNormal()
            self.normals[k] = face.getNormal()

            face = Face.Face(self.vertex[1], self.vertex[j], self.vertex[k])
            self.normals.append(face.getNormal())

            self.normals[j] = face.getNormal()
            self.normals[k] = face.getNormal()


        self.normals[1] = [0,1,0]


        self.ebo = EBOGL.EBOGL(vertex=self.vertex, index=self.indexs, normals=self.normals)

    def draw(self):
        if self.shader:
            self.shader.use()
            super().writeMatrixs(self.shader)
        self.ebo.draw()