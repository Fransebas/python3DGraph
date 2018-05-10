import EBOGL
import glm
from OpenGL.GL import *
from Texture import *


class Function():

    def __init__(self, f):
        self.ebo = None
        self.f = f
        self.points = []
        self.indexs = []
        self.colors = []
        self.coords = []

        self.xRange = 20
        self.yRange = 20

        self.M = glm.mat4(1.0)

        self.texture = Texture("./Textures/texture.png")

        self.abg = [1.0,0.0,0.0]

        self.__build__()


    def __build__(self):
        scaleX = 1/self.xRange
        scaleZ = 1/self.yRange

        flag = True

        for i in range(0,self.xRange):
            for j in range(0, self.yRange):
                x = scaleX*i - scaleX*self.xRange/2.0
                z = scaleZ*j - scaleZ*self.yRange/2.0
                y = self.f(x, z)
                self.points.append((x,y,z))

                if flag:
                    self.colors.append([1.0,0.0,1.0])
                else:
                    self.colors.append([0.0, 1.0, 0.0])

                flag = not flag



        for i in range(0,self.xRange-1):
            for j in range(0, self.yRange-1):
                a = i*self.yRange + j
                b = a + 1
                c = (i+1)*(self.yRange) + j
                d = c + 1

                #print( "(a,b,c,d) = ", (a,b,c,d) )



                self.indexs.append(a)
                self.indexs.append(b)
                self.indexs.append(c)

                self.indexs.append(b)
                self.indexs.append(c)
                self.indexs.append(d)

        coord = [[[0.0, 0.0], [0.5, 0.0], [1.0, 0.0]] , [[0.0, 1.0], [0.5, 1.0], [1.0, 1.0]]]

        for i in range(0,self.xRange):
            for j in range(0, self.yRange):
                if i%2 == 0:
                    self.coords.append(coord[0][i % 3])
                else:
                    self.coords.append(coord[1][i % 3])

        #self.ebo = EBOGL.EBOGL(self.points, self.indexs, self.colors, self.coords)
        self.ebo = EBOGL.EBOGL(self.points, self.indexs, self.coords)

    def setRotation(self, abg):
        self.abg = abg

    def setAalpha(self, a):
        self.abg[0] = a

    def setBeta(self, b):
        self.abg[1] = b

    def setGama(self, c):
        self.abg[2] = c


    def rotAalpha(self, a):
        self.abg[0] += a

    def rotBeta(self, b):
        self.abg[1] += b

    def rotGama(self, c):
        self.abg[2] += c

    def __generateMatrix__(self):
        self.M = glm.mat4(1.0)
        self.M = glm.rotate(self.M, self.abg[0], glm.vec3(1, 0, 0))
        self.M = glm.rotate(self.M, self.abg[1], glm.vec3(0, 1, 0))
        self.M = glm.rotate(self.M, self.abg[2], glm.vec3(0, 0, 1))



    def draw(self, program = None):
        self.__generateMatrix__()
        #self.texture.bind()
        if program:
            program.setMat4(self.M)
        self.ebo.draw()



