import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import requests
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWebChannel import QWebChannel

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.showFullScreen()  # Show the window in full-screen mode
    sys.exit(app.exec_())
