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
            self.mainlayout.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(63, 76, 107, 255), stop:1 rgba(63, 76, 107, 255)); border-radius:50px")
            self.center()
            self.oldPos = self.pos()
            self.initUI()
            self.equalRoundCorners()

        def initUI(self):
            self.searchInput = QLineEdit(self)
            self.searchInput.setGeometry(70,750,300,50)
            self.searchInput.setStyleSheet("border-radius:25")
            self.searchInput.setFont(QFont("Arial",17))
            self.searchInput.setAlignment(Qt.AlignCenter)

            self.AddToQueryButton = QPushButton(self)
            self.AddToQueryButton.setGeometry(390,750,75,50)
            self.AddToQueryButton.setText("Add To Query")
            self.AddToQueryButton.setFont(QFont("Arial",14))
            self.AddToQueryButton.setStyleSheet("QPushButton{background-color:#dd1123; border-radius:25px;}\
                                            QPushButton:hover{background-color:#ef3343;}\
                                            QPushButton:pressed{background-color:#ed1b2d}")
            self.AddToQueryButton.clicked.connect(self.AddToQuery)


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
            
            
        
        def AddToQuery(self):
            try:
                if(self.searchInput.text().strip()) == "":
                    self.errorDialog.showMessage("Search Input is Empty")
                else:
                    raw_request = requests.get("https://www.youtube.com/results?search_query="+self.searchInput.text().strip().replace(" ","+"))
                    print(raw_request.text)
            except:
                self.errorDialog.showMessage("Wrong Search Type")


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
        
        #
        def equalRoundCorners(self):
            self.topleftButton = QLabel(self)
            self.topleftButton.setGeometry(0,0,50,50)
            self.topleftButton.setStyleSheet("background-color:rgba(63, 76, 107, 255); border-top-left-radius:25px;")
            self.bottomleftButton = QLabel(self)
            self.bottomleftButton.setGeometry(0,814,50,50)
            self.bottomleftButton.setStyleSheet("background-color:rgba(63, 76, 107, 255); border-bottom-left-radius:25px;")
            self.bottomrightButton = QLabel(self)
            self.bottomrightButton.setGeometry(1230,814,50,50)
            self.bottomrightButton.setStyleSheet("background-color:rgba(63, 76, 107, 255); border-bottom-right-radius:25px;")


    def runApp():
        app = QApplication(sys.argv)
        window = dailyReminder()
        window.show()
        sys.exit(app.exec())

    runApp()
if __name__ == "__main__":
    main()

