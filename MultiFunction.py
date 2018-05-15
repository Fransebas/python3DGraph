import EBOGL
import glm
from OpenGL.GL import *
from Texture import *
from Face import *
from Drawable import  *
from Function import *
from Shaders import *


class MultiFunction(Drawable):

    def __init__(self, strf):
        super().__init__()
        self.scale = 5
        self.ebo = None

        self.shader = Shader()
        self.shader.addFragment("shaders/fragment.frag")
        self.shader.addVertex("shaders/fragment.vert")
        self.shader.compile()

        self.f = Function(strf, type=Function.Types.MULT_FUNC)
        self.points = []
        self.indexs = []
        self.coords = []
        self.normals = []

        self.xRange = 10
        self.yRange = 10

        self.texture = Texture("Textures/texture3.png")

        self.__build__()

    def getFunction(self):
        return self.f


    def __build__(self):
        scaleX = self.scale/self.xRange
        scaleZ = self.scale/self.yRange

        m = 3

        for i in range(0,self.xRange):
            for j in range(0, self.yRange):
                x = scaleX*i - scaleX*self.xRange/2.0
                z = scaleZ*j - scaleZ*self.yRange/2.0
                y = self.f.eval(x, z)
                self.points.append((x,y,z))

                self.coords.append([ i*0.5, j*0.5])

                self.normals.append([0.0, 0.0, 0.0])

        for i in range(0,self.xRange-1):
            for j in range(0, self.yRange-1):
                a = i*self.yRange + j
                b = a + 1
                c = (i+1)*(self.yRange) + j
                d = c + 1

                f = Face(self.points[a], self.points[b], self.points[c])
                self.normals[a] = f.getNormal()
                self.normals[b] = f.getNormal()
                self.normals[c] = f.getNormal()
                self.normals[d] = f.getNormal()

                self.indexs.append(a)
                self.indexs.append(b)
                self.indexs.append(c)

                self.indexs.append(b)
                self.indexs.append(c)
                self.indexs.append(d)

        #self.ebo = EBOGL.EBOGL(self.points, self.indexs, self.colors, self.coords)
        self.ebo = EBOGL.EBOGL(vertex=self.points, index=self.indexs, textCoords=self.coords, normals=self.normals)



    def draw(self):
        if self.shader:
            self.shader.use()
            super().writeMatrixs(self.shader)
            self.texture.bind()
        self.ebo.draw()



