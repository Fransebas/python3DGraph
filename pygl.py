from OpenGL.GL import *
from OpenGL.arrays import vbo
from VBOGL import *
from EBOGL import *
import function
from Shaders import *
import time
import glfw

from OpenGL.GL import *
import math

def fxy(x,y):
    return math.sin(10*x)*math.cos(10*y)/5.0

class Window():
    """Creates a simple vertex shader..."""

    def __init__(self):

        self.initWindos()

        self.shader = Shader()
        self.shader.addVertex("./shaders/fragment.vert")
        self.shader.addFragment("./shaders/fragment.frag")


        self.shader.compile()
        self.f = function.Function(fxy)
        self.dt = 0.1

        glEnable(GL_DEPTH_TEST)



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

    def Render(self):

        while True:
            glfw.poll_events()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


            t1 = time.time()

            self.shader.use()

            self.f.draw(self.shader)
            self.f.rotBeta(self.dt * 0.5)
            #self.f.rotAalpha(self.dt * 0.1)
            #self.f.setGama(self.dt * 1)
            #finally:
            #self.shader.clear()

            glfw.swap_buffers(self.window)

            self.dt = time.time() - t1



if __name__ == "__main__":
    window = Window()
    window.Render()