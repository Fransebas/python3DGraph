from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QListWidgetItem
from Function import *


class FunctionListQT(QWidget):

    def __init__(self, f, parent, i, item, deleteCallBack = None):
        super().__init__(parent)
        self.f = f
        self.i = i
        self.item = item
        self.deleteCallBack = deleteCallBack
        self.createWidgets()
        self.initGridLayout()

    def createWidgets(self):
        self.title = QLabel("Function")
        self.typeLable = QLabel(self.f.getType())
        self.name = QLabel(str(self.f))
        self.deleteButton = QPushButton('Delete')
        self.deleteButton.clicked.connect(self.onDeleteClick)


    def initGridLayout(self):
        layout = QGridLayout()

        layout.addWidget(self.title, 0,0)
        layout.addWidget(self.typeLable, 1,0)
        layout.addWidget(self.name, 2,0)
        layout.addWidget(self.deleteButton, 2, 2)

        self.setLayout(layout)

    @pyqtSlot()
    def onDeleteClick(self):
        if self.deleteCallBack:
            self.deleteCallBack(self.i, self.item)