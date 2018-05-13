from OpenGL.GL import *
from OpenGL.arrays import vbo
from VBOGL import *
from EBOGL import *
import function
import Parametric
from Shaders import *
import time
import glfw
import Axis
import Vector
import VectorField

import Geometry.Cone

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

from Camera import Camera

from OpenGL.GL import *
import math

def fxy(x,y):
    return x**2 + y**2

def tanF(x,y):
    return 2*0.2*x + 2*0.3*y - fxy(0.3,0.2)

def pf2(t):
    return [t,t**2,0]

def vf(x,y,z):
    return [y+2*z, x-z, 2*x-y]

def pf(t):
    q = 7
    p = 3
    u = 25*t
    return [math.cos(t) * (q + p * math.cos(u)), p * math.sin(u), math.sin(t) * (q + p * math.cos(u))]
    #return [ c*( math.cos(t)) + a*math.cos(t*15), c*math.sin(t*15), c*math.sin(t) ]


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


class openGL():

    def __init__(self):

        self.initWindos()

        self.shader = Shader()
        self.shader.addVertex("./shaders/fragment.vert")
        self.shader.addFragment("./shaders/fragment.frag")

        self.drawingElements = []
        self.shader.compile()

        self.dt = 0.1

        self.dx = 0
        self.dy = 0
        self.x = 0
        self.y = 0

        self.camera = Camera()

        self.isClick = False

        glEnable(GL_DEPTH_TEST)

        self.initElements()
        self.glEnables()

    def glEnables(self):
        #glEnable(GL_LINE_SMOOTH)

        glLineWidth(1)

    def initElements(self):
        #self.drawingElements.append(function.Function(fxy, self.shader))
        #self.drawingElements.append(function.Function(tanF, self.shader))
        self.drawingElements.append(Parametric.Parametric(pf, (0, 2 * 3.1416), 400))
        self.drawingElements.append(Axis.Axis())
        self.drawingElements.append(VectorField.VectorField(vf))
        #self.drawingElements.append(Vector.Vector([-2,3,4], start=[1,1,1]))
        #self.drawingElements.append(Parametric.Parametric(pf2, (-5,5), 25))

    def initWindos(self):

        if not glfw.init():
            return

        # version hints
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)


        self.window = glfw.create_window(800, 600, "My OpenGL window", None, None)

        if not self.window:
            glfw.terminate()
            return

        glfw.make_context_current(self.window)

        glfw.set_cursor_pos_callback(self.window, self.cursor)
        glfw.set_mouse_button_callback(self.window, self.cursorClick)


    def cursorClick(self, window, button, action, mods):

        if button == glfw.MOUSE_BUTTON_LEFT:
            if glfw.PRESS == action:
                self.isClick = True
                self.dx = 0
                self.dy = 0
            elif glfw.RELEASE == action:
                self.isClick = False


    def cursor(self, window, x, y):

        if self.isClick:
            self.dx = self.x - x
            self.dy = self.y - y

        self.x = x
        self.y = y

    def Render(self):

        while True:
            glfw.poll_events()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


            t1 = time.time()

            self.camera.rotBeta(min(self.dt * self.dx, 0.05))
            self.camera.rotAalpha(min(self.dt * self.dy, 0.05))

            for e in self.drawingElements:
                e.setV(self.camera.getV())
                e.draw()
                #e.rotBeta(min(self.dt * self.dx, 0.05) )
                #e.rotAalpha(min(self.dt * self.dy, 0.05) )



            #finally:
            #self.shader.clear()

            glfw.swap_buffers(self.window)

            self.dt = time.time() - t1





if __name__ == "__main__":
    gl = openGL()
    #

    app = QApplication(sys.argv)

    window = Window()

    gl.Render()

    sys.exit(app.exec_())

