from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from PyQt5.QtGui import *
from pytube import YouTube
import requests
import sys


def main():
    class dailyReminder(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Daily Reminder")
            self.setGeometry(300,50,1280,864)
            self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
            self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
            self.mainlayout = QFrame(self)
            self.mainlayout.setGeometry(0,0,1280,864)
            self.mainlayout.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(15, 32, 39, 255), stop:0.5 rgba(32, 58, 67, 255), stop:1 rgba(44, 83, 100, 255)); border-radius:50px")
            self.center()
            self.oldPos = self.screen().availableGeometry().center()
            self.initUI()


        def initUI(self):
            self.searchInput = QLineEdit(self)
            self.searchInput.setGeometry(100,150,350,50)
            self.searchInput.setStyleSheet("border-radius:25")
            self.searchInput.setFont(QFont("Arial",17))
            self.searchInput.setPlaceholderText("Video Link Goes Here")
            self.searchInput.setAlignment(Qt.AlignCenter)

            self.searchVideoButton = QPushButton(self)
            self.searchVideoButton.setGeometry(100,215,350,50)
            self.searchVideoButton.setText("Search For Video")
            self.searchVideoButton.setFont(QFont("Arial",14))
            self.searchVideoButton.setStyleSheet("QPushButton{background-color:#dd1123; border-radius:25px;}\
                                            QPushButton:hover{background-color:#ef3343;}\
                                            QPushButton:pressed{background-color:#ed1b2d}")
            self.searchVideoButton.clicked.connect(self.SearchVideo)
        #===========================================Video Search Output layout for add queue======================================#
            self.videolayout = QFrame(self)
            self.videolayout.setGeometry(100,280,350,500)
            self.videolayout.setStyleSheet("background-color:#99f2c8; border-radius:25px")

            self.videoNameLabel = QLabel(self.videolayout)
            self.videoNameLabel.setGeometry(75,20,200,50)
            self.videoNameLabel.setStyleSheet("background-color:#c6f8e0")
            self.videoNameLabel.setText("Video Name")
            self.videoNameLabel.setFont(QFont("Arial",20))
            self.videoNameLabel.setAlignment(Qt.AlignCenter)

            self.videoNameDisplay = QLabel(self.videolayout)
            self.videoNameDisplay.setGeometry(25,65,300,50)
            self.videoNameDisplay.setAlignment(Qt.AlignCenter)
            self.videoNameDisplay.setFont(QFont("Arial",13))
            self.videoNameDisplay.setWordWrap(True)

            self.QualitySelection = QComboBox(self)
            self.QualitySelection.setGeometry(200,530,150,35)
            self.QualitySelection.setStyleSheet("background-color:#FFEFBA")            
        #=================================================================================================================#

        #===========================================================Close and Hide Buttons=======================================#
            self.closeButton = QPushButton(self)
            self.closeButton.setGeometry(1230,0,50,50)
            self.closeButton.setStyleSheet("QPushButton{background-color:#dd1123; border-top-right-radius:25px;}\
                                            QPushButton:hover{background-color:#ef3343;}\
                                            QPushButton:pressed{background-color:#ed1b2d}")
            self.closeButton.setText("✖️")
            self.closeButton.setFont(QFont("Arail",15))
            self.closeButton.clicked.connect(self.close)

            self.hideButton = QPushButton(self)
            self.hideButton.setGeometry(1180,0,50,50)
            self.hideButton.setStyleSheet("QPushButton{background-color:#dd6611; color:black; border-bottom-left-radius:25px;}\
                                            QPushButton:hover{background-color:#ef8133;}\
                                            QPushButton:pressed{background-color:#ed721b}")
            self.hideButton.setText("➖")
            self.hideButton.setFont(QFont("Arail",15))
            self.hideButton.clicked.connect(self.showMinimized)

            self.errorDialog = QErrorMessage(self)
            self.errorDialog.setWindowTitle("Error")
            
            self.clearFocusButton = QPushButton(self)
            self.clearFocusButton.setGeometry(0,0,0,0)
            self.clearFocusButton.setFocus()
        #============================================================================================================================#
            
            
        
        def SearchVideo(self):
            videoSearchText = self.searchInput.text()
            videoSearchText.replace(" ","")
            if videoSearchText == "":
                self.errorDialog.showMessage("Link Input is Empty","Error")
            elif "youtube" in videoSearchText:
                try:
                    self.tempVideo = YouTube(videoSearchText)
                    title = self.tempVideo.title
                    self.videoNameDisplay.setText(title)
                    self.QualitySelection.addItems()
                except:
                    self.errorDialog.showMessage("Wrong Link","Error")
            else:
                try:
                    self.tempVideo = YouTube("https://www.youtube.com/watch?v="+videoSearchText)
                    title = self.tempVideo.title
                    self.videoNameDisplay.setText(title)
                except:
                    self.errorDialog.showMessage("Wrong Link","Error")

            



        #======================dragging frameless window==================#
        def mouseMoveEvent(self, event):
            delta = QPoint (event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        def mousePressEvent(self, event):
            self.oldPos = event.globalPos()
        def center(self):
            qr = self.frameGeometry()
            cp = self.screen().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
        #=================================================================#
        

    def runApp():
        app = QApplication(sys.argv)
        window = dailyReminder()
        window.show()
        sys.exit(app.exec())

    runApp()
if __name__ == "__main__":
    main()
