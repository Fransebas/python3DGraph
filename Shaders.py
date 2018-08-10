from OpenGL.GL import shaders
from OpenGL.GL import *
import glm

class Shader():

    def __init__(self):
        self.vertex = None
        self.fragment = None
        self.shader = glCreateProgram()


    def compile(self):
        glAttachShader(self.shader, self.vertex)
        glAttachShader(self.shader, self.fragment)
        glLinkProgram(self.shader)
        #self.shader = shaders.compileProgram(self.vertex, self.fragment)


    def addVertex(self, fileName):
        f = open(fileName, "r")
        s = ""
        for l in f:
            s += l
        self.vertex = shaders.compileShader(s, GL_VERTEX_SHADER)

    def addFragment(self, fileName):
        f = open(fileName, "r")
        s = ""
        for l in f:
            s += l
        self.fragment = shaders.compileShader(s, GL_FRAGMENT_SHADER)

    def use(self):
        shaders.glUseProgram(self.shader)

    def clear(self):
        shaders.glUseProgram(0)

    def setMat4(self, mat, str):
        glUniformMatrix4fv(glGetUniformLocation(self.shader, str), 1, GL_FALSE, glm.value_ptr(mat))

    def setVec4(self, vect, str):
        glUniform4fv(glGetUniformLocation(self.shader, str), 1, glm.value_ptr(vect))

    def setVec3(self, vect, str):
        glUniform3fv(glGetUniformLocation(self.shader, str), 1, glm.value_ptr(vect))
