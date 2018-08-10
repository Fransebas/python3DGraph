import glm

from sympy.core.singleton import Singleton

class Camera():
    """
    The Camera object is simpler object that in most OpenGL programs
    Here the camera is static and acts only as a rotation matrix
    """

    V = glm.mat4(1.0)
    abg = [0.0, 0.0, 0.0]
    s = [1.0, 1.0, 1.0]

    def __init__(self):
        print ("Camera created")
        pass

    def setRotation(self, abg):
        Camera.abg = abg

    def setAalpha(self, a):
        Camera.abg[0] = a

    def setBeta(self, b):
        Camera.abg[1] = b

    def setGama(self, c):
        Camera.abg[2] = c


    def rotAalpha(self, a):
        Camera.abg[0] += a

    def rotBeta(self, b):
        Camera.abg[1] += b

    def rotGama(self, c):
        Camera.abg[2] += c

    def setScale(self, s):
        Camera.s = s

    def __generateMatrix__(self):
        Camera.V = glm.mat4(1.0)

        Camera.V = glm.scale(Camera.V, glm.vec3(Camera.s[0], Camera.s[1], Camera.s[2]))

        Camera.V = glm.translate(Camera.V, glm.vec3(0.0, 0.0, -2.0))

        Camera.V = glm.rotate(Camera.V, Camera.abg[0], glm.vec3(1, 0, 0))
        Camera.V = glm.rotate(Camera.V, Camera.abg[1], glm.vec3(0, 1, 0))
        Camera.V = glm.rotate(Camera.V, Camera.abg[2], glm.vec3(0, 0, 1))



    def getV(self):
        self.__generateMatrix__()
        return Camera.V