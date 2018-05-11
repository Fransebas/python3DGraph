import glm

class Drawable():

    def __init__(self):
        self.M = glm.mat4(1.0)
        self.P = glm.perspective(glm.radians(50.0), 1,  0.1, 10.0 );
        self.V = glm.translate(glm.mat4(1.0), glm.vec3(0.0, 0.0, -2.0))

        self.abg = [0.0, 0.0, 0.0]

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

    def writeMatrixs(self, shader):
        if shader:
            shader.setMat4(self.M, "M")
            shader.setMat4(self.P, "P")
            shader.setMat4(self.V, "V")

    def __generateMatrix__(self):
        self.M = glm.mat4(1.0)
        self.M = glm.rotate(self.M, self.abg[0], glm.vec3(1, 0, 0))
        self.M = glm.rotate(self.M, self.abg[1], glm.vec3(0, 1, 0))
        self.M = glm.rotate(self.M, self.abg[2], glm.vec3(0, 0, 1))