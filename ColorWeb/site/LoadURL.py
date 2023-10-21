import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import requests, time


def CheckIsURl(url):
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
            if CheckIsURl("http://localhost:8000/"):            
                break
            else:
                continue


        self.browser.setUrl(QUrl("http://localhost:8000/"))

        # Set the window properties
        self.setWindowTitle("Color Energy Detect")
        # Adjust the window size as needed
        self.setGeometry(100, 100, 800, 600)
        # Remove the minimize button from the window
        # Remove the Maximize button
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)


        # Add the browser widget to the main window
        self.setCentralWidget(self.browser)
        # Set the background color to white using CSS
        self.browser.setStyleSheet("background-color: #f0f0f0;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.showMaximized()  # Show the window in full-screen mode
    sys.exit(app.exec_())

