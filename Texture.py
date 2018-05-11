from PIL import Image
from OpenGL.GL import *
import numpy as np

class Texture():

    def __init__(self, name):
        self.image = Image.open(name)
        #self.image.convert('RGB')
        self.imageData =  np.asarray(self.image, np.uint8)
        self.initMemory()


    def initMemory(self):
        self.textureGLUINT = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D,self.textureGLUINT)

        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
                     self.image.width, self.image.height, 0, GL_RGB,
                     GL_UNSIGNED_BYTE, self.imageData)

    def bind(self):
        glBindTexture(GL_TEXTURE_2D, self.textureGLUINT)

    def unbind(self):
        glBindTexture(GL_TEXTURE_2D, 0)