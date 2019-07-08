from OpenGL.GL import *
from OpenGL.arrays import vbo
from PyQt5 import QtOpenGL
from PyQt5.QtCore import pyqtSlot, QTimer

from VBOGL import *
from EBOGL import *
import MultiFunction
import Parametric
from Shaders import *
import time
import Axis
import Vector
import VectorField

import Geometry.Cone

from Function import *

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QOpenGLWidget, QGridLayout, QGroupBox, QLineEdit, QPushButton, \
    QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon, QOpenGLContext, QSurfaceFormat, QOpenGLVersionProfile

from gui import functionListQT

from Camera import Camera

from OpenGL.GL import *
import math


def fxy(x, y):
    return x ** 2 + y ** 2


def tanF(x, y):
    return 2 * 0.2 * x + 2 * 0.3 * y - fxy(0.3, 0.2)


def pf2(t):
    return [t, t ** 2, 0]


def vf(x, y, z):
    return [y + 2 * z, x - z, 2 * x - y]


def pf(t):
    q = 7
    p = 3
    u = 25 * t
    return [math.cos(t) * (q + p * math.cos(u)), p * math.sin(u), math.sin(t) * (q + p * math.cos(u))]
    # return [ c*( math.cos(t)) + a*math.cos(t*15), c*math.sin(t*15), c*math.sin(t) ]


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Graphy'
        self.left = 10
        self.top = 10
        self.width = 810
        self.height = 610
        self.functionList = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createWidgets()
        self.initGridLayout()
        self.initEvent()
        self.show()

    def createWidgets(self):
        self.glWidget = openGL(self)
        self.glWidget.resize(800, 600)
        self.textbox = QLineEdit(self)
        self.functionListW = QListWidget(self)
        self.addEqButton = QPushButton('Add')

    def initGridLayout(self):
        layout = QGridLayout()

        layout.setColumnStretch(0, 10)
        layout.setRowStretch(0, 10)
        layout.addWidget(self.glWidget, 0, 0)
        layout.addWidget(self.textbox, 1, 0)
        layout.addWidget(self.addEqButton, 1, 1)
        layout.addWidget(self.functionListW, 0, 1)

        self.setLayout(layout)

    def initEvent(self):
        self.addEqButton.clicked.connect(self.onAddClick)

    def addElementToList(self):
        i = self.glWidget.getElementsSize() - 1
        item = QListWidgetItem(self.functionListW)
        customWidget = functionListQT.FunctionListQT(self.glWidget.getFunction(i).getFunction(), self, i, item,
                                                     self.deleteFunction)
        item.setSizeHint(customWidget.sizeHint())
        self.functionListW.addItem(item)
        self.functionListW.setItemWidget(item, customWidget)

    def deleteFunction(self, i, item):
        self.functionListW.takeItem(self.functionListW.row(item))
        # self.functionListW.removeItemWidget( item )
        # widget.deleteLater()
        self.glWidget.removeFunction(i)
        pass

    def processExpresion(self, str):
        """

        :param str: str
        :return:
        """
        fullExp = str.split(":")
        exp = fullExp[0]
        if (len(fullExp) > 1):
            if fullExp[1].replace(" ", "") == "Parametric":
                type = Function.Types.PARAMETRIC
            elif fullExp[1].replace(" ", "") == "VField":
                type = Function.Types.VECTOR
        else:
            type = Function.Types.MULT_FUNC

        return (exp, type)

    @pyqtSlot()
    def onAddClick(self):
        textboxValue = self.textbox.text()
        try:
            exp, type = self.processExpresion(textboxValue)
            self.glWidget.addFunction(exp, type)
            self.addElementToList()
        finally:
            self.textbox.setText("")


class openGL(QtOpenGL.QGLWidget):

    def initializeGL(self):

        self.initElements()
        self.glEnables()

    def __init__(self, parent):
        fmt = QtOpenGL.QGLFormat()
        fmt.setVersion(3, 3)
        fmt.setProfile(QtOpenGL.QGLFormat.CoreProfile)
        fmt.setSampleBuffers(True)

        super().__init__(fmt, parent)

        timer = QTimer(parent)
        timer.timeout.connect(self.updateGL)
        timer.start(0)

        self.drawingElements = []

        self.dt = 0.1

        self.dx = 0
        self.dy = 0
        self.ds = 1
        self.x = 0
        self.y = 0
        self.draw = True

        self.camera = Camera()

        self.isClick = False

    def removeFunction(self, i):
        self.drawingElements.pop(i)

    def getElementsSize(self):
        return len(self.drawingElements)

    def getFunction(self, i):
        return self.drawingElements[i]

    def addFunction(self, strf, type):
        try:
            if type == Function.Types.MULT_FUNC:
                self.drawingElements.append(MultiFunction.MultiFunction(strf))
            elif type == Function.Types.PARAMETRIC:
                self.drawingElements.append(Parametric.Parametric(strf, (0, 2 * np.pi), 200))
            elif type == Function.Types.VECTOR:
                self.drawingElements.append(VectorField.VectorField(strf))
        finally:
            pass

    def glEnables(self):
        glEnable(GL_DEPTH_TEST)
        glLineWidth(1)

    def initElements(self):
        self.drawingElements.append(Axis.Axis())

    def cursorClick(self, window, button, action, mods):
        pass
        """if button == glfw.MOUSE_BUTTON_LEFT:
            if glfw.PRESS == action:
                self.isClick = True
                self.dx = 0
                self.dy = 0
            elif glfw.RELEASE == action:
                self.isClick = False"""

    def wheelEvent(self, QWheelEvent):
        super().wheelEvent(QWheelEvent)
        self.ds += self.dt * (QWheelEvent.angleDelta().y()/8.0)

    def cursor(self, x, y):

        if self.isClick:
            # self.updateGL()
            self.dx = self.x - x
            self.dy = self.y - y

        self.x = x
        self.y = y

    def mousePressEvent(self, QMouseEvent):
        self.isClick = True
        self.dx = 0
        self.dy = 0
        self.x = QMouseEvent.x()
        self.y = QMouseEvent.y()

    def mouseReleaseEvent(self, QMouseEvent):
        self.isClick = False

    def mouseMoveEvent(self, QMouseEvent):
        self.cursor(QMouseEvent.x(), QMouseEvent.y())

    def paintEvent(self, QPaintEvent):
        # self.updateGL()
        pass

    def paintGL(self):
        t1 = time.time()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.camera.rotBeta(min(self.dt * self.dx, 0.1))
        self.camera.rotAalpha(min(self.dt * self.dy, 0.1))
        self.camera.setScale([self.ds, self.ds, self.ds])


        for e in self.drawingElements:
            e.setV(self.camera.getV())
            e.draw()

        self.dt = time.time() - t1

        self.draw = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # gl = openGL()
    window = Window()

    # gl.Render()

    sys.exit(app.exec_())
