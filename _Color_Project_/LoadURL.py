import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import requests
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtGui import QIcon  # Import QIcon
from PyQt5.QtGui import QCursor  # Import QCursor from QtGui
def CheckIsURL(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        while True:
            if CheckIsURL("http://localhost:8000/"):
                break
            else:
                continue

        self.browser.setUrl(QUrl("http://localhost:8000/"))

        self.setWindowTitle("Color Energy Detect")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setCentralWidget(self.browser)
        self.browser.setStyleSheet("background-color: #f0f0f0;")



        # # Create and style the Quit button
        # quit_button = QPushButton("Quit", self)
        # quit_button.clicked.connect(QApplication.instance().quit)
        # quit_button.setGeometry(1775, 7, 80, 30)
        # quit_button.setStyleSheet(
        #     """
        #     background-color: #fff;
        #     border: 2px solid #000;
        #     color: #000;
        #     font-family: Inter,sans-serif;
        #     font-size: 16px;
        #     font-weight: 600;
        #     text-align: center;
        #     padding: 0 17px;
        #     min-width: 80px;
        #     height: 48px;
        #     justify-content: center;
        #     align-items: center;
        #     display: inline-flex;
        #     cursor: pointer;
        #     user-select: none;
        #     -webkit-user-select: none;
        #     touch-action: manipulation;
        #     margin-left:10px
        #     """
        # )

        # quit_button.setCursor(QCursor(Qt.PointingHandCursor))  # Change cursor to a hand on hover

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.showFullScreen()  # Show the window in full-screen mode
    sys.exit(app.exec_())
