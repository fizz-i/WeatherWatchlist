import requests
import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGraphicsDropShadowEffect)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPixmap,QPalette, QBrush, QLinearGradient, QColor)
from dotenv import load_dotenv
import random
from Weather_page import Page1
from Movie_page import Page2

class WeatherWatchlist(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget(self)
        self.page1 = Page1(self.stack)
        self.page2 = Page2(self.stack)

        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)
        
        self.setStyleSheet("background: linear-gradient(to right, #11998e, #38ef7d);")
        
        #gradient
        
        gradient = QLinearGradient(0, 0, self.width(), 0)  # Horizontal
        gradient.setColorAt(0.0, QColor("#d3d3d3"))  # Start
        gradient.setColorAt(1.0, QColor("#808080"))  # End

        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setAutoFillBackground(False)
        self.setPalette(palette)


        layout  = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)
        self.setWindowTitle("WeatherWatchlist")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_ = WeatherWatchlist()
    app_.show()
    sys.exit(app.exec_())
