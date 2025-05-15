import requests
import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from dotenv import load_dotenv



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
        self.setWindowTitle("WeatherWatchlist")

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
                background-color: #2c3e50;
                color: white;
                border-radius: 12px;
                padding: 10px 20px;
                font-size: 14px;
                
                }
            
            QPushButton#GetButton:hover {
                background-color: #34495e;
            }
            
            QPushButton#GetButton:pressed {
                background-color: #1abc9c;
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
        


class Page2(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        back_button = QPushButton("Back")
        back_button.clicked.connect(self.go_to_page1)

    def initUI(self):   #Initial UI to be set, CSS, Get Pictures somehow
        pass
    
    def to_getMovie(self): ##TMDB API to be connected
        pass

    def to_displayError(self): #error handling
        pass

    #funtion to display error

    def go_to_page1(self):
        self.stacked_widget.setCurrentIndex(0)

class WeatherWatchlist(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget(self)
        self.page1 = Page1(self.stack)
        self.page2 = Page2(self.stack)

        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)
        self.setStyleSheet("background-color: #b2f7ef;")
        layout  = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_ = WeatherWatchlist()
    app_.show()
    sys.exit(app.exec_())
