import time

import pyautogui
from PIL import ImageQt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys
import cv2
from pynput import mouse

class Epic7Calculator(QWidget):
    def __init__(self):
        super(Epic7Calculator, self).__init__()
        self.setParameter()
        self.setGUI()
        self.show()

    def setParameter(self):
        self.title = 'Epic 7 Equipment Calculator'
        self.messageTitle = 'screen capture'
        self.messageContent = 'drag area for screenshot'

        # initialize
        self.captureStart = False

    def setGUI(self):
        # set title
        self.setWindowTitle(self.title)

        # initialize main layout
        mainLayout = QVBoxLayout()

        # initialize img view
        self.imageView = QLabel()
        mainLayout.addWidget(self.imageView)

        # set button layout
        buttonLayout = QHBoxLayout()
        browseButton = QPushButton("browse")
        browseButton.clicked.connect(self.browse)
        captureButton = QPushButton("capture")
        captureButton.clicked.connect(self.capture)
        calculateButton = QPushButton("calculate")
        calculateButton.clicked.connect(self.calculate)
        buttonLayout.addWidget(browseButton)
        buttonLayout.addWidget(captureButton)
        buttonLayout.addWidget(calculateButton)

        # add button layout to main layout
        mainLayout.addLayout(buttonLayout)

        # set main layout
        self.setLayout(mainLayout)

    def browse(self):
        # get file name with QFileDialog(jpg or png)
        fname = QFileDialog.getOpenFileName(self, 'open img', './', 'img file(*.jpg *.png)')

        # get file path
        imgPath = fname[0]

        # update image view
        self.imageView.setPixmap(QPixmap(imgPath))


    def capture(self):
        reply = QMessageBox.question(self, self.messageTitle, self.messageContent,
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.captureStart = True
            self.pressed = False

            # initilize image view
            self.imageView.setPixmap(QPixmap())

            # make full screen and transparent background for mouse click event
            self.showFullScreen()
            self.setWindowOpacity(0.2)

        else:
            return

    def mousePressEvent(self, e):

        if e.buttons() & Qt.LeftButton and self.captureStart == True:
            self.x1 = e.x()
            self.y1 = e.y()
            self.pressed = True

    def mouseReleaseEvent(self, e):

        if self.captureStart == True and self.pressed == True:
            self.x2 = e.x()
            self.y2 = e.y()

            # capture dragged area
            # calculate each point and width, height
            leftTopX = min(self.x1, self.x2)
            leftTopY = min(self.y1, self.y2)
            width = abs(self.x1 - self.x2)
            height = abs(self.y1 - self.y2)

            # save temp image, cause there was issue with converting image instance
            pyautogui.screenshot("./temp.png", region=(leftTopX, leftTopY, width, height))

            # update image view
            self.imageView.setPixmap(QPixmap("./temp.png"))

            # turn off transperency
            self.showNormal()
            self.setWindowOpacity(1)
            self.captureStart = False

    def calculate(self):
        pass

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    ex = Epic7Calculator()
    sys.exit(app.exec())
