import requests
import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGraphicsDropShadowEffect)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPixmap,QPalette, QBrush, QLinearGradient, QColor)
from dotenv import load_dotenv
import random




class Page1(QWidget):
 
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.weather_label = QLabel(self)
        self.weatherdesc = QLabel("HOT",self)
        self.weather_emooji = QLabel("HOTEMOJI",self)
        self.get_movie_button = QPushButton("Get a Movie For this Weather",self)
        
        self.UI1()


    def UI1(self):
        

        vbox = QVBoxLayout()
        vbox.addWidget(self.weather_label)
        vbox.addWidget(self.weatherdesc)
        vbox.addWidget(self.weather_emooji)
        vbox.addWidget(self.get_movie_button)
        
        self.setLayout(vbox)
        self.weather_label.setAlignment(Qt.AlignCenter)
        self.weatherdesc.setAlignment(Qt.AlignCenter)
        self.weather_emooji.setAlignment(Qt.AlignCenter)

        self.weather_label.setObjectName("WeatherLabel")
        self.weatherdesc.setObjectName("weatherdesc")
        self.weather_emooji.setObjectName("emoji")
        self.get_movie_button.setObjectName("GetButton")
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(25)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(QColor(0,0,0,150))
        
        self.weather_label.setGraphicsEffect(shadow)
        self.weatherdesc.setGraphicsEffect(shadow)
        self.weather_emooji.setGraphicsEffect(shadow)
        self.get_movie_button.setGraphicsEffect(shadow)
        

        self.setStyleSheet("""  
            QLabel, QPushButton {
                font-family: Helvetica Neue;
                           }

            QLabel#WeatherLabel {
                font-size: 62px;
                font-style: bold;
                color: #2c3e50;
                           }
            
            QLabel#weatherdesc {
                font-size: 58px;
                font-weight: Demi bold;
                color: #2c3e50;
                           }

            QLabel#emoji {
                font-size: 60px;
                font-family: Noto Color Emoji;
                           }

            QPushButton#GetButton {
    background: qlineargradient(
        x1:0, y1:0, x2:0, y2:1,
        stop:0 #00b894,
        stop:1 #019875);
    color: white;
    border-radius: 10px;
    padding: 12px 25px;
    font-size: 16px;
    font-weight: 600;
    border: none;

}

QPushButton#GetButton:hover {
    background: qlineargradient(
        x1:0, y1:0, x2:0, y2:1,
        stop:0 #019875,
        stop:1 #00b894);

}

QPushButton#GetButton:pressed {
    background: #01775c;

}


""") #ADD DROP SHADOW, Better Front, Better Background 
        
        self.get_movie_button.clicked.connect(self.go_to_page2)
        self.get_weather()
        self.setMinimumSize(400,300)
        self.resize(500,400)

    def Location(self):                                   #ERROR Handling is pending
        res = requests.get("https://ipinfo.io/json")
        data = res.json()
        city = data.get("city")
        return city

    def get_weather(self):                         #Error handling is pending
        load_dotenv()
        api_key = os.getenv("api_key")
        city = self.Location()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"


        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["cod"]==200:
            self.display_weather(data)

    def go_to_page2(self):
        self.stacked_widget.setCurrentIndex(1)

    def display_weather(self,data):
        temp = data["main"]["temp"]
        real_temp = temp - 273
        desc = data["weather"][0]["description"]
        weather_id  = data["weather"][0]["id"]
        print(data)

        self.weather_label.setText(f"{round(real_temp)}°C {self.Location()}")
        self.weatherdesc.setText(f"{desc}")
        self.weather_emooji.setText(f"{self.get_emoji(weather_id)}")

    
    #Another function to display errors

    @staticmethod
    def get_emoji(weather_id):
        if weather_id >= 200:
            return "⛈️"
        elif weather_id >= 300:
            return "🌧️"
        elif weather_id >= 500:
            return "🌧️"
        elif weather_id >= 600:
            return "❄️"
        elif weather_id >= 700:
            return "🌫️"
        elif weather_id == 800:
            return "☀️"
        elif weather_id > 800:
            return "☁️"
        
